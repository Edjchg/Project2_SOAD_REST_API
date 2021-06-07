package com.database.mongo;

import com.database.connection.Person;
import com.google.gson.Gson;
import com.database.connection.MongoConnection;
import com.google.gson.GsonBuilder;
import com.sun.tools.classfile.ConstantPool;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import java.util.Arrays;
import java.util.List;

@Path("/mongodb")
public class MongoResource {

    @GET
    @Path("/test")
    @Produces("text/plain")
    public String hello() {
        return "Mongo API is up!";
    }

    @GET
    @Path("/nlpInsert/{jsonInfo}")
    @Produces("application/json")
    public String nlp_insert(@PathParam("jsonInfo") String jsonInfo){
        // {[{"person_name": "andrey", "times": 3, "filename": "test"}, {"person_name": "edgar", "times": 3, "filename": "test"}]}
        Gson gson = new Gson();
        Person[] personList = gson.fromJson(jsonInfo, Person[].class);

        if(personList.length == 0){
            return "";
        }

        MongoConnection mongoDb = new MongoConnection();
        mongoDb.set_mongo_server_name("mongodb");
        mongoDb.set_data_base_name("nlp");              //Nombre de la base de MONGO
        mongoDb.set_server_ip("localhost");
        mongoDb.set_server_port("27017");
        mongoDb.set_collection_name(personList[0].get_filename());
        mongoDb.insert(personList);
        return "ok";

        //System.out.println(listPerson.get(0).get_person_name());
        //return analyzer.get_people_list_json();
    }
}