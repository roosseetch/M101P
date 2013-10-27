use enron

// Solution One
db.messages.aggregate([
	   {$unwind: "$headers.To"},
	   // {$sort: {"headers.From": 1, "headers.To": 1}},
	   {$match:
         {
           // $and: [{"headers.From": "andrew.fastow@enron.com"}, {"headers.To": "john.lavorato@enron.com"}],
           $and: [{"headers.From": "andrew.fastow@enron.com"}, {"headers.To": "jeff.skilling@enron.com"}],
         }
       },
       {$sort: {"city": 1}},
       {$group:
         {
           _id: null,
           "num_of_messages": {$sum: 1}
         }
       },
       {$project:
         {
          "_id": 0,
          "num_of_messages":1
         }
       }
])

// Solution Two
db.messages.find({"headers.From":"andrew.fastow@enron.com","headers.To":"jeff.skilling@enron.com"}).count()
