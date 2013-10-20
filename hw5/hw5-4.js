use states
db.zips.aggregate([
       {$sort: {"city": 1}},
       {$project:
         {
          "pop":1,
           first_char: {$substr : ["$city",0,1]}
         }
       },
       {$match:
         {
           // first_char: {$in: ["0","1","2","3","4","5","6","7","8","9"]}
           first_char: {$lt: "A"}
         }
       },
       {$group:
         {
           _id: null,
           pop: {$sum:"$pop"}
         }
       }
])
