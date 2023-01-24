console.log("hi")
var root= document.compatMode=='BackCompat'? document.body : document.documentElement;
if (root.scrollHeight>root.clientHeight) {
    console.log("scrollbar appeared lmao")
    document.getElementsByClassName("container-fluid d-flex mt-2 mb-2").style.minHeight = "calc(46vh - 3rem)";
    document.getElementsByClassName("btn pink flex-fill d-flex flex-column align-items-center justify-content-center my-2 text-light").style.height = "calc(46vh - 3rem)";
}
console.log("hi")