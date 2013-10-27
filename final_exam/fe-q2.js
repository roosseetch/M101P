use enron
db.messages.aggregate([
	   {$unwind: "$headers.To"},
       {$group:
         {
           "_id": {"_id":"$_id", "headers_From": "$headers.From"},
           headers_To: { $addToSet: "$headers.To" }
         }
       },
	   {$unwind: "$headers_To"},
       {$group:
         {
           "_id": {"headers_From": "$_id.headers_From", "headers_To": "$headers_To"},
           "num_of_messages": {$sum: 1}
         }
       },
       // {$match:
       //   {
       //     "_id.headers_From": "andrew.fastow@enron.com"
       //   }
       // },
       {$project:
         {
          "_id": 1,
          "num_of_messages":1
         }
       },
	   // {$sort: {"num_of_messages": 1, "_id.headers_From": 1, "_id.headers_To": 1}},
	   {$sort: {"num_of_messages": -1}},
       {$limit: 5}
])
