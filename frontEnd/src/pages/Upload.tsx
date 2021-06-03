import React, { useState, useEffect } from 'react';
import Path from 'path';
import uploadFileToBlob, { isStorageConfigured } from './storage-blob';
import * as contName from './storage-blob';

const storageConfigured = isStorageConfigured();
const acc = localStorage.getItem("account");
const listDocument: string[] = [];
let userA = localStorage.getItem("account");
export var containerName = (userA || '');

const UploadDocument = (): JSX.Element => {
  useEffect(() => {
    async function getLink() {
      var Hearders = {
        'Accept': '*/*',
        'Content-Type': 'text/plain',
        'user': containerName
      };
      const response = await fetch('http://localhost:4000/Link', {
      method : 'GET',
      headers : new Headers (Hearders)
    });
    const json = await response.json();
    console.log(json);
    }
    getLink();
  }, []);

  // all blobs in container
  const [blobList, setBlobList] = useState<string[]>([]);

  // current file to upload into container
  const [fileSelected, setFileSelected] = useState(null);

  // UI/form management
  const [uploading, setUploading] = useState(false);
  const [inputKey, setInputKey] = useState(Math.random().toString(36));

  const [ hasError, setHasError ] = useState(false);

  const onFileChange = (event: any) => {
    // capture file into state
    setFileSelected(event.target.files[0]);
  };

  async function post(file : any) {
    try {
      // http://localhost:9080/Gradle__com_example__api_1_0_SNAPSHOT_war/api/storage/{'+contName.containerName+': '', '+impFileName+': ''}'
        // Create request to api service
        console.log("Account: " + localStorage.getItem("account"));
        console.log("Container: " + contName.containerName);
        const req = await fetch('http://localhost:9080/Gradle___com_example___api_1_0_SNAPSHOT_war/api/storage/{\'containerName\': '+ contName.containerName +', \'filename\': '+ file +'}', {
            /*
            method: 'POST',
            headers: { 'Content-Type':'application/json' },
            
            // format the data
            body: JSON.stringify({

            }),*/
        });
        
        const res = await req.json();

        // Log success message
        console.log(res);                
    } catch(err) {
        console.error(`ERROR: ${err}`);
    }
}
  const onFileUpload = async () => {
    // prepare UI
    setUploading(true);

    // *** UPLOAD TO AZURE STORAGE ***
    const blobsInContainer: string[] = await uploadFileToBlob(fileSelected);
    
    // prepare UI for results
    setBlobList(blobsInContainer);

    //post(blobsInContainer[blobsInContainer.length - 1].split(/(\\|\/)/g).pop());
    console.log("marcador: " + localStorage.getItem('nameFile'));
    post(localStorage.getItem('nameFile'));
    //console.log("Nombre del archivo: " + blobsInContainer[blobsInContainer.length - 1].split(/(\\|\/)/g).pop());

    // reset state/form
    setFileSelected(null);
    setUploading(false);
    setInputKey(Math.random().toString(36));
  };

  // display form
  const DisplayForm = () => (
    <div>
      <input type="file" onChange={onFileChange} key={inputKey || ''} />
      <button type="submit" onClick={onFileUpload}>
        Upload!
          </button>
    </div>
  )

  // display file name
  const DisplayNameFileFromContainer = () => (
    <div>
      <h2>Container items</h2>
      <ul>
        {blobList.map((item) => {
          //listDocument = blobList;
          return (
            <li key={item}>
              <div>
                {Path.basename(item)}
                <br />
              </div>
            </li>
          );
        })}
      </ul>
    </div>
  );

  return (
    <div>
      <h1>Upload file to Analize</h1>
      {storageConfigured && !uploading && DisplayForm()}
      {storageConfigured && uploading && <div>Uploading</div>}
      <hr />
      {storageConfigured && blobList.length > 0 && DisplayNameFileFromContainer()}
      {!storageConfigured && <div>Storage is not configured.</div>}
    </div>
  );
};

export default UploadDocument;
