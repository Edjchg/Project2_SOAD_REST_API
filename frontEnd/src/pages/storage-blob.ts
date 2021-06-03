import { BlobServiceClient, ContainerClient} from '@azure/storage-blob';


const sasToken = process.env.storagesastoken || "sv=2020-02-10&ss=bfqt&srt=sco&sp=rwdlacupx&se=2021-04-24T05:47:07Z&st=2021-04-23T21:47:07Z&spr=https,http&sig=lAL%2BkPnSvQlvvO%2BUmasZBrnt2uERNYA%2F3UUJJSSi8jg%3D"; // Fill string with your SAS token
let a = localStorage.getItem("account")?.toLowerCase();
console.log("min: " + a);
export var containerName = (a || '');
// account name as the name of the container
//localStorage.setItem('account', localStorage.getItem("account"));
//console.log("imp: " + localStorage.getItem("account"));
//export const containerName = (a || '');
console.log("2: " + containerName);
const storageAccountName = process.env.storageresourcename || "soadocument"; // Fill string with your Storage resource name
// </snippet_package>

// <snippet_isStorageConfigured>
// Feature flag - disable storage feature to app if not configured
export const isStorageConfigured = () => {
  return (!storageAccountName || !sasToken) ? false : true;
}
// </snippet_isStorageConfigured>

// <snippet_getBlobsInContainer>
// return list of blobs in container to display
const getBlobsInContainer = async (containerClient: ContainerClient) => {
  const returnedBlobUrls: string[] = [];

  // get list of blobs in container
  // eslint-disable-next-line
  for await (const blob of containerClient.listBlobsFlat()) {
    // if image is public, just construct URL
    returnedBlobUrls.push(
      `https://${storageAccountName}.blob.core.windows.net/${containerName}/${blob.name}`
    );
  }
  return returnedBlobUrls;
}

export const getBlobNames = async (contName: string) => {
  const blobService = new BlobServiceClient(
    `https://${storageAccountName}.blob.core.windows.net/?${sasToken}`
  );
  const containerClient: ContainerClient = blobService.getContainerClient(contName);
  const blobNames = [];

  // get list of blobs in container
  for await (const blob of containerClient.listBlobsFlat()) {
    // if image is public, just construct URL
    blobNames.push(blob.name);
  }
  return blobNames;
}

// </snippet_getBlobsInContainer>

// <snippet_createBlobInContainer>
const createBlobInContainer = async (containerClient: ContainerClient, file: File) => {
  
  // create blobClient for container
  const blobClient = containerClient.getBlockBlobClient(file.name);

  // set mimetype as determined from browser with file upload control
  const options = { blobHTTPHeaders: { blobContentType: file.type } };

  // upload file
  await blobClient.uploadBrowserData(file, options);
}

export const impFileName = async (file: File | null): Promise<string> => {
  if (!file) return "";
  return file.name;
}
// </snippet_createBlobInContainer>

// <snippet_uploadFileToBlob>
const uploadFileToBlob = async (file: File | null): Promise<string[]> => {
  if (!file) return [];
  impFileName(file);
  console.log("...: " + file.name);
  localStorage.setItem('nameFile', file.name);

  // get BlobService = notice `?` is pulled out of sasToken - if created in Azure portal
  const blobService = new BlobServiceClient(
    `https://${storageAccountName}.blob.core.windows.net/?${sasToken}`
  );

  // get Container - full public read access
  const containerClient: ContainerClient = blobService.getContainerClient(containerName);
  await containerClient.createIfNotExists({
    access: 'container',
  });

  // upload file
  await createBlobInContainer(containerClient, file);

  // get list of blobs in container
  return getBlobsInContainer(containerClient);
};
// </snippet_uploadFileToBlob>

export default uploadFileToBlob;