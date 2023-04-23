let enter = document.querySelector(".enter")
let outer = document.querySelector(".outer")
let run = document.querySelector(".run")
let langE = document.querySelector(".langE")
let langS = document.querySelector(".langS")
langE.value = "french"
langS.value = "english"
let text = ""
enter.value = ""
outer.value = ""
run.addEventListener("click",(e)=>{
    let xhr = new XMLHttpRequest()
    outer.value = "Traduction en cours...."
   xhr.addEventListener("readystatechange",()=>{
       if(xhr.readyState == 4){
           let res = xhr.responseText
           res = JSON.parse(res)
           outer.value = res.text
       }
   })
    xhr.open("GET",window.location.href+"translate?text="+enter.value+"&langE="+langE.value+"&langS="+langS.value)
    xhr.send()
})
