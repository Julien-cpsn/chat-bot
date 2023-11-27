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

/* === VARIABLES === */

var logs = []
var session = new QiSession()
var tts = undefined
var language = "English"
var LanguageManager = undefined
var ALMemory = undefined
var AlignmentMatrix = undefined


/* === SERVICES === */

session.service("ALMemory").then(function (local_ALMemory) {
    ALMemory = local_ALMemory
});

session.service("ALTextToSpeech").then(function (local_tts) {
    // tts is a proxy to the ALTextToSpeech service
    tts = local_tts
    tts.setLanguage("English")
})

session.service("AlignmentMatrix").then(function (local_alignment_matrix) {
    AlignmentMatrix = local_alignment_matrix
})

session.service("LanguageManager").then(function (local_language_manager) {
    LanguageManager = local_language_manager
})

/* === MAIN === */

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
        tts.say(sentences["click"][language] + data.replace("_", " ").replace("ch", "k"))

        AlignmentMatrix[data]()

        debug(data)
    })

    $("img[lang]").click(async function () {
        language = $(this).attr("lang")

        await LanguageManager.setLanguage(language)
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