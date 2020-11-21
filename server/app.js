const express = require("express"),
    request = require("request"),
    firebase = require('firebase/app');;
var app = express();
app.use(express.json());
let url = "https://dsci551-a1e31.firebaseio.com/Movie_info_result/.json"


//跨域问题
app.all('*', function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Content-Type,Content-Length, Authorization, Accept,X-Requested-With");
    res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
    res.header("X-Powered-By",' 3.2.1')
    if(req.method=="OPTIONS") res.send(200);/*让options请求快速返回*/
    else  next();
});

//get addr address data from angular and return weather info
app.get("/test", function(req, res){
    console.log(req.query);
    request(url, (err, response)=>{
        // console.log(response.body)
        res.send(response.body);
    })
    
});

// app.get("/test", function(req, res){
//     console.log(req.query);
//     res.send({
//         "Actors" : [ "Roy Scheider", "Robert Shaw", "Richard Dreyfuss", "Lorraine Gary" ],
//         "Awards" : "Won 3 Oscars. Another 11 wins & 20 nominations.",
//         "BoxofficeAnalysis" : {
//           "Domestic Gross(in dollars)" : 102247150,
//           "Domestic Opening Gross(in dollars)" : 0,
//           "Domestic Percent" : 38.2,
//           "Foreign Gross(in dollars)" : 165200000,
//           "Foreign Percent" : 61.8,
//           "Opening Percent" : 0,
//           "Rest Percent" : 100,
//           "Result Percent" : 100
//         },
//         "Country" : "USA",
//         "Director" : "Steven Spielberg",
//         "Genre" : [ "Adventure", "Thriller" ],
//         "Language" : "English",
//         "Plot" : "When a killer shark unleashes chaos on a beach community, it's up to a local sheriff, a marine biologist, and an old seafarer to hunt the beast down.",
//         "Poster" : "https://m.media-amazon.com/images/M/MV5BMmVmODY1MzEtYTMwZC00MzNhLWFkNDMtZjAwM2EwODUxZTA5XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg",
//         "Rated" : "PG",
//         "Ratings" : [ {
//           "Source" : "Internet Movie Database",
//           "Value(out of 10)" : 8.0
//         }, {
//           "Pecentage Value(out of 100%)" : 98.0,
//           "Source" : "Rotten Tomatoes"
//         }, {
//           "Source" : "Metacritic",
//           "Value(out of 100)" : 87
//         } ],
//         "Released" : "20 Jun 1975",
//         "Runtime" : "124 min",
//         "Title" : "Jaws",
//         "Type" : "movie",
//         "Writer" : [ "Peter Benchley (screenplay)", "Carl Gottlieb (screenplay)", "Peter Benchley (based on the novel by)" ],
//         "Year" : "1975",
//         "imdbVotes" : 538009
//     })
    
// });

app.listen(8081, process.env.IP, function(){
    console.log("The Weather Search Server Has Started!");
 });

 