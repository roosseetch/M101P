use enron

db.messages.update(
	   {"headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>"},
       { $push: { "headers.To": "mrpotatohead@10gen.com" }}, {multi: true}
);

db.messages.find({"headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>"},
 {"headers.From": 1, "headers.To": 1, "headers.Message-ID": 1, "_id":0}).limit(4).pretty();
