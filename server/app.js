const { stdout, stderr } = require("process");

const express = require("express"),
    request = require("request"),
    // firebase = require('firebase/app'),
    util = require('util'),
    exec = require('child_process').exec;
var app = express();
app.use(express.json());
let url = "https://dsci551-b9bb2.firebaseio.com/%s/.json",
    actor_firebase = "Actor_info_result",
    movie_firebase = "Movie_info_result",
    boxof_firebase = "Box_office_ranking_result"


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
// app.get("/Actor's_Name", function(req, res){
//     var actor_url = util.format(url, actor_firebase);
//     var file = "../calculation/webpage1_actor.py"
//     var name = req.query.input
//     var name_new = '"' + name.split(" ").join(" ") +'"'
//     var cmd = util.format("python %s %s", file, name_new)
//     exec(cmd, (err, stdout, stderr)=>{
//         if(err) console.log(err);
//         else if (stdout) {
//             request(actor_url, (err, response)=>{
//                 console.log(response.body)
//                 res.send(response.body);
//             })
//         }
//         else console.log(stderr)
//     })
// });


app.get("/Actor's_Name", function(req, res){
    var actor_url = util.format(url, actor_firebase);
    var file = "../calculation/webpage1_actor.py"
    var name = req.query.input
    var name_new = '"' + name.split(" ").join(" ") +'"'
    var cmd = util.format("python %s %s", file, name_new)
    // exec(cmd, (err, stdout, stderr)=>{
    //     if(err) console.log(err);
    //     else if (stdout) {
            request(actor_url, (err, response)=>{
                console.log(response.body)
                res.send(response.body);
            })
        // }
        // else console.log(stderr)
    // })
});

app.get("/Movie_Title", function(req, res){
    var movie_url = util.format(url, movie_firebase);
    var file = "../calculation/webpage2_movie.py"
    var title = req.query.input
    var title_new = '"' + title.split(" ").join(" ") +'"'
    var cmd = util.format("python %s %s", file, title_new)
    // exec(cmd, (err, stdout, stderr)=>{
    //     if(err) console.log(err);
    //     else if (stdout) {
            request(movie_url, (err, response)=>{
                console.log(response.body);
                res.send(response.body);
            })
        // }
    //     else console.log(stderr)
    // })
});

// app.get("/Movie_Title", function(req, res){
//     var movie_url = util.format(url, movie_firebase);
//     var file = "../calculation/webpage2_movie.py"
//     var title = req.query.input
//     var title_new = '"' + title.split(" ").join(" ") +'"'
//     var cmd = util.format("python %s %s", file, title_new)
//     exec(cmd, (err, stdout, stderr)=>{
//         if(err) console.log(err);
//         else if (stdout) {
//             request(movie_url, (err, response)=>{
//                 res.send(response.body);
//             })
//         }
//         else console.log(stderr)
//     })
// });


app.get("/Released_Year", function(req, res){
    console.log(req.query);
    var year_url = util.format(url, boxof_firebase)
    request(year_url, (err, response)=>{
        if(err) console.log(err)
        // console.log(response.body)
        res.send(response.body);
    })
    
});

//监听端口8081
app.listen(8081, process.env.IP, function(){
    console.log("The Weather Search Server Has Started!");
 });

 