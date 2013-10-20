use school
db.students.aggregate([
       {$unwind: "$scores"},
       {$match:
         {
           "scores.type": {$in: ["exam", "homework"]},
         }
       },
       {$group:
         {
           _id: {"student_id": "$student_id", "class_id": "$class_id"},
           "avg_st_score_in_cls": {$avg:"$scores.score"}
         }
       },
       {$group:
         {
           _id: "$_id.class_id",
           "avg_cls_score": {$avg:"$avg_st_score_in_cls"}
     }
   },
   {$sort: {"avg_cls_score" : -1}},
   {$project:
     {
	 _id:0,
	 "class_id":"$_id",
	 "avg_cls_score": 1
     }
    },
   {$limit:1}
])
