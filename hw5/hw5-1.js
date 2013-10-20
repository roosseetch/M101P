use blog
db.posts.aggregate([
    {$unwind: "$comments"},
    {$group:
      {
        _id: {author_comments:"$comments.author"},
        numComments: {$sum:1}
      }
    },
    {$sort:
      {"numComments":-1}
    },
    {$project:
     {
     _id:0,
     "commentator":"$_id.author_comments"
     }
    },
    { $limit : 1 }
])
