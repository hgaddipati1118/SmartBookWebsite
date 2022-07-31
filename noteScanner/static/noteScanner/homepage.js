const webcamElement = document.getElementById('webcam');
const canvasElement = document.getElementById('canvas');
const snapSoundElement = document.getElementById('snapSound');
const webcam = new Webcam(webcamElement, 'user', canvasElement, snapSoundElement);
webcam.start()
  .then(result =>{
    console.log("webcam started");
  })
  .catch(err => {
    console.log(err);
});
let picture = webcam.snap();
var today = new Date();
var todayNum = Math.floor(today.getTime());
document.getElementById("title").value = todayNum;
function saveFile() {
    var link = document.createElement("a");
    console.log(todayNum)
    console.log(today)
    let pork = document.getElementById("canvas");
    let image = pork.toDataURL('image/png').replace('image/png', 'image/octet-stream');
    document.body.appendChild(link); // for Firefox
    link.setAttribute("href", image);
    link.setAttribute("download", "SmartBookPic"+document.getElementById("title").value+".jpg");
    link.click();
    console.log(document.getElementById("hiddenSubmit").hidden)
    document.getElementById("hiddenSubmit").hidden = false;
}

let skipPart = () => {
  let url = window.location.href;
  url = url + "/processImage";
  console.log(url)
  window.location.href = url;
}
