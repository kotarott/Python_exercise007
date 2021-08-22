$("#translate_words").on("click", function() {
    const values = words.value
    const from_lang = $("#from_lang").val()
    const to_lang = $("#to_lang").val()
    if (values) {
        async function run() {
            let result = await eel.translate(values, from_lang, to_lang)();
            add_result(result)
        }
        run();
    } else {
        alert("テキストが入力されていません。")
    }
})

function add_result(values) {
    translated_words.value = values
}