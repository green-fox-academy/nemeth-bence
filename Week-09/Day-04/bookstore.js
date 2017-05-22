'use strict';

const mysql = require("mysql");
const express = require("express");
const app = express();

var conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: "bookstore"
});

const querybooks = "SELECT book_name FROM book_mast"

const queryallbooks = "SELECT book_mast.book_name, author.aut_name, category.cate_descrip, publisher.pub_name, book_mast.book_price FROM book_mast " +
'LEFT JOIN author ON book_mast.aut_id = author.aut_id ' +
'LEFT JOIN category ON book_mast.cate_id = category.cate_id ' +
'LEFT JOIN publisher ON book_mast.pub_id = publisher.pub_id '


app.get('/listbooks', function get(req, res) {
    var HTML = "<ul>"
    conn.query(querybooks, function(err,rows){
        if(err) {
            console.log("Something went wrong.", err);
        } else {
            rows.forEach(row => {
                HTML += "<li>" + row.book_name + "</li>";
            });
            HTML += "</ul>"
        }
        res.send(HTML);
    });
});

app.get('/allbooks', function get(req, res) {
  var category = req.query.category;
  var publisher = req.query.publisher;
  var plt = req.query.plt;
  var pgt = req.query.pgt;
  var queryfilter = queryallbooks;

if ((category) || (publisher) || (plt) || (pgt)){
    queryfilter += 'WHERE ';
    if (category) {
      queryfilter += "category.cate_descrip = '" + category + "' AND "
    }
    if (publisher) {
      queryfilter += "publisher.pub_name = '" + publisher + "' AND "
    }
    if (plt) {
      queryfilter += "book_mast.book_price < '" + plt + "' AND "
    }
    if (pgt) {
      queryfilter += "book_mast.book_price > '" + pgt + "' AND "
    }
    queryfilter = queryfilter.slice(0,-4);
  }


    conn.query(queryfilter, function(err,rows){
        if(err) {
            console.log("Something went wrong.", err);
        } else {
          var HTML = "<table><tr><th>Book title</th><th>Authors name</th><th>Category</th><th>Publisher name</th><th>Price</th></tr>"
            rows.forEach(row => {
                HTML += "<tr><td>" + row.book_name + "</td><td>" + row.aut_name + "</td><td>" + row.cate_descrip + "</td><td>" + row.pub_name + "</td><td>" + row.book_price + "</td></tr>";
            });
            HTML += "</table>"
        }
        console.log(queryfilter)
        res.send(HTML);
        queryfilter = queryallbooks;
    });
});

app.listen(3000, function () {
    console.log('server running');
})
