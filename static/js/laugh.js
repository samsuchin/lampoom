const laugh_btn = document.getElementById("laugh")
const work_pk = document.getElementById("work-pk").value;
const endpoint = document.getElementById("laugh-endpoint").value;
laugh_btn.addEventListener("click", (e)=>{
    if(laugh()){
    confetti()
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
        console.log(localStorage.getItem("laughs_pk"))
        console.log(localStorage.getItem("laughs_count"))
        document.getElementById("laugh-score").innerHTML = data.score
    })
}
})

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
        laugh_btn.append(c)
    }
}

function laugh(){
    var laughs_pk = localStorage.getItem("laughs_pk")
    var laughs_count = localStorage.getItem("laughs_count")
    if (!laughs_pk){
        localStorage.setItem('laughs_pk', work_pk);
        localStorage.setItem('laughs_count', 1);
        return true
    }
    if (laughs_pk.split(",").includes(work_pk)){
        let index = laughs_pk.split(",").indexOf(work_pk)
        let laughs_count_list = laughs_count.split(",")
        if(laughs_count_list[index] < 10){
            laughs_count_list[index]++
            localStorage.setItem('laughs_count', laughs_count_list.join()); 
            return true;
        }
        else{
            console.log("cant like more than 10")
            return false;
        }
    }
    else{
        localStorage.setItem('laughs_pk', laughs_pk + "," + work_pk); 
        localStorage.setItem('laughs_count', laughs_count + "," + 1); 
        return true;
    }
}