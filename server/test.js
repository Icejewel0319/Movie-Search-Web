var exec = require('child_process').exec;
var arg1 = 'hello';
var arg2 = 'world';
var filename = 'server.py'
exec('python'+' '+filename+' '+arg1+' '+arg2,function(err,stdout,stderr){
    if(err)
    {
        console.log('stderr',err);
    }
    if(stdout)
    {
        console.log('stdout',stdout);
    }

});