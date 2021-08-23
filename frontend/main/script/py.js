let settingpage = 1
document.getElementById("setting-page").innerHTML = settingpage
let voiceCount = 0
async function bottomFunc(){
    let textVoiceStat = document.querySelector('.statusInfo4')
    let res = await eel.starterVoice(voiceCount)()
    if(res === 1){
        textVoiceStat.innerHTML = 'Производится'
        textVoiceStat.style.color = '#00A86B'
        voiceCount = 1
    }else{
        textVoiceStat.innerHTML = 'Не производится'
        textVoiceStat.style.color = 'rgb(255, 0, 0)'
        voiceCount = 0
    }
}
async function bottomFunc1(){
    let streamlink = document.getElementById("browser_video")
    let inputSetting = await eel.outputsetting()()
    let newlink = "http://"+inputSetting[0]+":"+inputSetting[1]+"/video"
    if (streamlink.src == newlink){
        newlink = "http://"+inputSetting[4]+":"+inputSetting[5]+"/video"
        streamlink.src = newlink
    }else{
        streamlink.src = newlink
    }
    
}

//setting to back
async function settingEnter1Func(){
    eel.ip1fun(document.getElementById('ipcamera1').value, settingpage)()
}
async function settingEnter2Func(){
    eel.port1fun(document.getElementById('portcamera1').value, settingpage)()
}
async function settingEnter3Func(){
    eel.login1fun(document.getElementById('logincamera1').value, settingpage)()
}
async function settingEnter4Func(){
    eel.password1fun(document.getElementById('passwordcamera1').value, settingpage)()
}


async function settingPage1(){
    let inputSetting = await eel.outputsetting()()
    document.getElementById("ipcamera1").placeholder =  inputSetting[0]
    document.getElementById("portcamera1").placeholder =  inputSetting[1]
    document.getElementById("logincamera1").placeholder =  inputSetting[2]
    document.getElementById("passwordcamera1").placeholder =  inputSetting[3]
}
async function settingPage2(){
    let inputSetting = await eel.outputsetting()()
    document.getElementById("ipcamera1").placeholder = inputSetting[4]
    document.getElementById("portcamera1").placeholder =  inputSetting[5]
    document.getElementById("logincamera1").placeholder =  inputSetting[6]
    document.getElementById("passwordcamera1").placeholder =  inputSetting[7]
}
//tcp python
//начинаем делать, когда будет готов манипулятор
async function forward(){
    //tcp code function python
}
async function back(){
    //tcp code function python
}
async function left(){
    //tcp code function python
}
async function right(){
    //tcp code function python
}
async function up(){
    //tcp code function python
}
async function down(){
    //tcp code function python
}
async function reset(){

}
//cv
async function cvjs(){
    eel.cv()()
}

//botton

jQuery('.btntop4').on('click', function(){
    bottomFunc()
})
jQuery('.btntop1').on('click', function(){
    bottomFunc1()
})
let scalestreamon = false
jQuery('#browser_video').on('click', function(){
    if (scalestreamon == false){
        document.getElementById("browser_video").style.transition = "transform .5s"
        document.getElementById("browser_video").style.transform = "translateX(100px) scale3d(2,2,2)"
        document.getElementById("browser_video").style.zIndex = "100"
        scalestreamon = true
    }else{
        document.getElementById("browser_video").style.transition = "transform .5s linear"
        document.getElementById("browser_video").style.transform = "scale3d(1,1,1)"
        document.getElementById("browser_video").style.zIndex = "1"
        document.getElementById("browser_video").style.transform = "translateX(0)"
        scalestreamon = false
    }
})

//setting btn
jQuery('#campage1').on('click', function(){
    document.getElementById("campage1").style.color = '#000'
	document.getElementById("campage2").style.color = '#FFF'
    settingpage = 1
    document.getElementById("setting-page").innerHTML = settingpage
    settingPage1()
})
jQuery('#campage2').on('click', function(){
    document.getElementById("campage2").style.color = '#000'
	document.getElementById("campage1").style.color = '#FFF'
    settingpage = 2
    document.getElementById("setting-page").innerHTML = settingpage
    settingPage2()
})


jQuery('.settingEnter1').on('click', function(){
    settingEnter1Func()
})
jQuery('.settingEnter2').on('click', function(){
    settingEnter2Func()
})
jQuery('.settingEnter3').on('click', function(){
    settingEnter3Func()
})
jQuery('.settingEnter4').on('click', function(){
    settingEnter4Func()
})
//tcp
jQuery('.btn1').on('click', function(){
    console.log("Вверх")
})
jQuery('.btn2').on('click', function(){
    console.log("Вправо")
})
jQuery('.btn3').on('click', function(){
    console.log("Вниз")
})
jQuery('.btn4').on('click', function(){
    console.log("Влево")
})
jQuery('.btn5').on('click', function(){
    console.log("Вверх")
})
jQuery('.btn6').on('click', function(){
    console.log("Вниз")
})
jQuery('.btn7').on('click', function(){
    console.log("Сброс")
})