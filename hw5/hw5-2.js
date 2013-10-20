use states

/* First Method */
db.zips.aggregate([
       // {$sort: {"state" :1, "city": 1, "pop": 1}},
       {$group:
         {
           _id: {state: "$state", city: "$city"},
           pop: {$sum:"$pop"}
         }
       },
       {$match:
         {
           "_id.state": {$in: ["CA", "NY"]},
           // "_id.state": /CA|NY/,
           // $or: [ { "_id.state":"CT" }, { "_id.state": "NJ"} ] ,
           // "_id.state": {$in: ["CT", "NJ"]},
           "pop":{$gt:25000}
         }
       },
       {$group:
         {
            /* _id:null mean go through all of the collection */
           _id:null,
           avg_pop: {$avg:"$pop"}
     }
   }
])


/* Second Method */
db.zips.aggregate([
       {$match:
         {
           "state": {$in: ["CA", "NY"]},
         }
       },
       {$group:
         {
           _id: {state: "$state", city: "$city"},
           pop: {$sum:"$pop"}
         }
       },
       {$match:
         {
           "pop":{$gt:25000}
         }
       },
       {$group:
         {
            /* _id:null mean go through all of the collection */
           _id:null,
           avg_pop: {$avg:"$pop"}
     }
   }
])
