
const video = document.getElementById("video");
const canvas = document.getElementById("overlay");
const expressionEl = document.getElementById("expressions")
Promise.all([
    faceapi.loadFaceExpressionModel("/static/models"),
    faceapi.loadSsdMobilenetv1Model("/static/models"),
]).then(startVideo)

function startVideo(){

    if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
      video.play()
      refreshState()
    })
    .catch(function (err) {
      console.log("Something went wrong!", err);
    });
}

}

async function refreshState() {
    setInterval(async() => {
        try{
            const detections = await faceapi.detectSingleFace(video).withFaceExpressions()
            console.log(detections.expressions)
            if (detections){
                console.log(detections.expressions)
                let happiness = Math.trunc(detections.expressions.happy * 100)
                let disgusted = Math.trunc(detections.expressions.disgusted * 100)
                document.getElementById("happiness").innerHTML = happiness
                document.getElementById("disgusted").innerHTML = disgusted
                drawResults(detections)
            }
        }
        catch(error){
            console.log(error)
        }
        

    }, 500)
}

function drawResults(detections){
      faceapi.matchDimensions(canvas, video)
      const resizedResults = faceapi.resizeResults(detections, video)
      const minConfidence = 0.05
      faceapi.draw.drawDetections(canvas, resizedResults)
}