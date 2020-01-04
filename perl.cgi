#!/usr/bin/perl
use CGI ':standard';
print "Content-type: text/html\n\n";

$first = param ('first');
$last = param ('last');
$power = param ('power');
$hero = param ('hero');
$cool = param ('cool');
$bench = param ('bench');
print"<html>";
print"<head>";
print (qq(<link href="https://fonts.googleapis.com/css?family=Supermercado+One&display=swap" rel="stylesheet">));
print (qq(<link href="https://fonts.googleapis.com/css?family=Staatliches&display=swap" rel="stylesheet">));
print (qq(<link href="https://fonts.googleapis.com/css?family=Anton&display=swap" rel="stylesheet">));
print"</head>";
print (qq(<br><br><div style = "font-family: 'Supermercado One', cursive;color: black;text-align: center;">));
print (qq(<h1>Hello <span style = "font-size: 160%;color: red;">$first $last </span>or shall I say <span style = "font-family: 'Anton', sans-serif;font-size: 180%;color: green">$hero</span> </h1>));
if ($bench eq "1") {
        print (qq(<h1>Oh I see you lift weights..... how <span style = "font-size: 160%;color: blue;">fascinating!!!!</span></h1>));
}
else{
        print(qq(<h1>You don't bench?!?!? What a <span style = "font-family: 'Staatliches', cursive;font-size: 140%;color: purple;">disgrace...</span></h1>));
}
if($cool eq "1"){
        print(qq(<h1>You seem <span style = "font-family: 'Staatliches', cursive;font-size 140%;color: cyan;">slick... </span>I respect that</h1>));
}
else{
        print(qq(<h1>You don't seem very <span style = "font-family: 'Staatliches', cursive;font-size 140%;color: cyan;">cool... </span></h1>));
}
print (qq(<br><br><br>));

print (qq(<h1 style = "font-size: 200%;">You have the power of .....</h1>));
print (qq(<br><h1 style = "font-size: 700%;color: orange;font-family: 'Anton', sans-serif;">$power</h1>));
print"</div>";
print"</html>";

