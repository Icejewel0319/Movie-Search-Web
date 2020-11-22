const express = require("express"),
    request = require("request"),
    // firebase = require('firebase/app'),
    util = require('util');
var app = express();
app.use(express.json());
let url = "https://dsci551-a1e31.firebaseio.com/%s/.json"


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
app.get("/Actor's_Name", function(req, res){
    console.log(req.query);
    request(url, (err, response)=>{
        // console.log(response.body)
        res.send({
            msg: "actor"
        });
    })
    
});
app.get("/Movie_Title", function(req, res){
    console.log(req.query);
    var movie_url = util.format(url, "Movie_info_result")
    request(movie_url, (err, response)=>{
        // console.log(response.body)
        res.send(response.body);
    })
    
});

app.get("/Released_Year", function(req, res){
    console.log(req.query);
    var year_url = util.format(url, "Box_office_ranking_result")
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

 