
const video = document.getElementById("video");
video.setAttribute("playsinline", true)
const canvas = document.getElementById("overlay");
const expressionEl = document.getElementById("expressions");
const video_view = document.getElementById("video-view");
const video_icon = document.getElementById("video-icon")
const endpoint = document.getElementById("laugh-endpoint").value;
const work_pk = document.getElementById("work-pk").value;

async function startLaughAnalysis(){
    Promise.all([
        faceapi.loadFaceExpressionModel("/static/models"),
        faceapi.loadSsdMobilenetv1Model("/static/models"),
    ]).then(startVideo)
}

function stopVideo(){
    var stream = video.srcObject;
    var tracks = stream.getTracks();
    for (var i = 0; i < tracks.length; i++) {
        var track = tracks[i];
        track.stop();
    }
    
    video.srcObject = null;
    canvas.style.display = "none"
    video.style.display = "none"
    document.getElementById("video-stop").style.display = "none";
    document.getElementById("video-start").style.display = "block";
}

function startVideo(){
    alert("Start reading the article with a straight face and only one face in the camera view.")
    if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
      video.play()
      video_view.style.display = "block"
      canvas.style.display = "block"
      video.style.display = "block"
        document.getElementById("video-stop").style.display = "block";
        document.getElementById("video-start").style.display = "none";
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
            if (detections){
                let happiness = Math.trunc(detections.expressions.happy * 100)
                drawResults(detections)
                if(happiness > 98){
                    confetti()
                    console.log("CONFETTI")
                    fetch(endpoint, {
                        method: 'POST',
                        headers: {
                            "X-CSRFToken": getCookie('csrftoken'),
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            work_pk: work_pk
                        }),
                    })
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById("laugh-score").innerHTML = data.score + " Laughs"
                        console.log(data)
                    })

                }
            }
        }
        catch(error){
            console.log(error)
        }
        

    }, 500)
}

function drawResults(detections){
    let happiness = Math.trunc(detections.expressions.happy * 100)
      faceapi.matchDimensions(canvas, video)
      const resizedResults = faceapi.resizeResults(detections, video)
      const minConfidence = 0.05
      faceapi.draw.drawDetections(canvas, resizedResults)   
      var ctx = canvas.getContext("2d");
    ctx.font = "20px Arial";
    ctx.fillStyle = "white";
    ctx.fillRect(0, canvas.height - 30, canvas.width, 30);
    ctx.fillStyle = "black";
    ctx.textAlign = "center";
    ctx.fillText("Happiness: " + happiness + "%", canvas.width/2, canvas.height - 10); 
}

function random(max){
    return Math.random() * (max - 0) + 0;
}

function confetti(){
    var c = document.createDocumentFragment();
    for (var i=0; i<100; i++) {
        var styles = 'transform: translate3d(' + (random(500) - 250) + 'px, ' + (random(200) - 150) + 'px, 0) rotate(' + random(360) + 'deg);\
                      background: hsla('+random(360)+',100%,50%,1);\
                      animation: bang 1000ms ease-out forwards;\
                      opacity: 0';
          
        var e = document.createElement("i");
        e.classList.add("conf")
        e.style.cssText = styles.toString();
        c.appendChild(e);
        video_view.append(c)
    }
}

