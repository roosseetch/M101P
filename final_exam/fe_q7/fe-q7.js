use photobase

// db.albums.ensureIndex( { images: 1 } )

function filter(image) {
	if (db.albums.count({'images': image._id}) == 0)
	{
		db.images.remove({'_id': image._id});
	}
};

function map() {
	emit('_id', this._id);
}

function reduce(key, values) {
	var result = 0;
	if (key === '_id') {
	    for(var i = 0; i < values.length; i++)
	    {
	        result += values[i];
	    }
	}
	return result;
}

db.images.find().forEach(filter);
db.images.mapReduce(map, reduce, {out: {inline: 1}});
