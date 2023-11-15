var sentences = {
    "selection": {
        "French": "Tu as selectionné ",
        "English": "You selected ",
    },
    "click": {
        "French": "Tu as cliqué sur ",
        "English": "You clicked on ",
    },
    "CPE": {
        "French": "c rien c CPE",
        "English": "it's nothing but CPE's management power"
    },
    "simplex": {
        "French": "C'est quoi Simplèxe ?",
        "English": "What is SimplX ?"
    },
    "language": {
        "French": "français",
        "English": "english",
    }
}

var logs = []
var session = new QiSession()
var tts = undefined
var language = "English"
var ALMemory = undefined

session.service("ALMemory").then(function (local_ALMemory) {
    ALMemory = local_ALMemory
});

session.service("ALTextToSpeech").then(function (local_tts) {
    // tts is a proxy to the ALTextToSpeech service
    tts = local_tts
    tts.setLanguage("English")
})

$(document).ready(function () {

    function debug(data) {
        logs.push(data)

        var text = ""
        for (var log of logs) {
            text += JSON.stringify(log)
            text += "<br>"
        }

        $("#debug").html(text)
    }

    $("td[id^=button-]").click(function () {
        var data = $(this).attr("app-action")
        tts.say(sentences["click"][language] + data.replace("-", " ").replace("ch", "k"))
        debug(data)
    })

    $("img[lang]").click(function () {
        language = $(this).attr("lang")
        tts.setLanguage(language)
        tts.say(sentences["selection"][language] + sentences["language"][language])
        debug(language)
    })

    $("#logo-sfr").click(function () {
        ALMemory.raiseEvent("play_sfr", null)
    })

    $("#logo-simplx").click(function () {
        tts.say(sentences["simplex"][language])
    })

    $("#logo-cpe-lyon").click(function () {
        tts.say(sentences["CPE"][language])
    })
})