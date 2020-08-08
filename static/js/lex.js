let dom = {
    lexWordInput : null,
    lexSearchButton : null,
    lexClearButton : null,
    lexUpdateButton : null,
    lexMakeLexicalDBButton : null,
    lexDicInfoDetails : null,


    probWordInput : null,
    probSearchButton : null,
    probClearButton : null,
    probUpdateButton : null,
    probMakeLexicalDBButton : null,
    probDicInfoDetails : null,

    loadingBox: null
};

/**
 * body onload = "init()"
 */
function init() {
    getDomReferences();
    registerListeners();
}

/**
 * dom 객체 레퍼런스를 가져온다.
 */
function getDomReferences() {
    dom.lexWordInput = document.getElementById("lexWordInput");
    dom.lexSearchButton = document.getElementById("lexSearchButton");
    dom.lexClearButton = document.getElementById("lexClearButton");
    dom.lexUpdateButton = document.getElementById("lexUpdateButton");
    dom.lexMakeLexicalDBButton = document.getElementById("MakeLexicalButton");
    dom.lexDicInfoDetails = document.getElementById("lexInfoDetails");

    dom.probWordInput = document.getElementById("probWordInput");
    dom.probSearchButton = document.getElementById("probSearchButton");
    dom.probClearButton = document.getElementById("probClearButton");
    dom.probUpdateButton = document.getElementById("probUpdateButton");
    dom.probMakeLexicalDBButton = document.getElementById("MakeProbButton");
    dom.probDicInfoDetails = document.getElementById("probInfoDetails");

    dom.loadingBox = document.getElementById("loadingBox");
}

/**
 * 이벤트 리스너를 등록한다.
 */
function registerListeners() {
    dom.lexSearchButton.addEventListener("click", onLexSearchButtonClick);
    dom.lexClearButton.addEventListener("click", onLexClearButtonClick);
    dom.lexUpdateButton.addEventListener("click", onLexUpdateButtonClick);
    dom.lexMakeLexicalDBButton.addEventListener("click", onMakeLexicalDBButton);

    dom.probSearchButton.addEventListener("click", onProbSearchButtonClick);
    dom.probClearButton.addEventListener("click", onProbClearButtonClick);
    dom.probUpdateButton.addEventListener("click", onProbUpdateButtonClick);
    dom.probMakeLexicalDBButton.addEventListener("click", onMakeProbDBButton);
}

// loading box function
function showLoadingBox() {
    dom.loadingBox.style.display = "inline-block";
}

function hideLoadingBox() {
    dom.loadingBox.style.display = "none";
}

// input values initialize
function onLexClearButtonClick(){
    dom.lexWordInput.value = null;
    dom.lexDicInfoDetails.value = null;
}
// input values initialize
function onProbClearButtonClick(){
    dom.probWordInput.value = null;
    dom.probDicInfoDetails.value = null;
}
function onLexSearchButtonClick(){
    postLexSearch();
}
function onProbSearchButtonClick(){
    postProbSearch();
}
function onLexUpdateButtonClick(){
    postLexUpdate();
}
function onProbUpdateButtonClick(){
    postProbUpdate();
}
function onMakeLexicalDBButton(){
    postMakeLexicalDB();
}
function onMakeProbDBButton(){
    postMakeProbDB();
}


function postLexSearch() {
    var data = {
        word : dom.lexWordInput.value
    };

    $.ajax({
        type: "POST",
        url: "/postLexSearch",
        data: JSON.stringify(data),
        dataType:'json' ,
        contentType: "application/json",
        success: function (response) {
            // if error has data => show error msg alert
            dom.dicInfoDetails.value = response.result;

            if (typeof(response.errors) != "undefined" && response.errors.length != 0 ) {
                alert((response.errors));
                dom.dicInfoDetails.value = response.errors;
            }
            // dom.dicInfoDetailsLeft.value = response.dicInfoLeft;
            //dom.dicInfoDetailsRight.value = response.dicInfoRight;
            // text.posTagged = response.result;
            // dom.dicInfoDetailsLeft.innerHTML = text.posTagged;

        }
    });
}

function postProbSearch() {
    var data = {
        word : dom.probWordInput.value
    };

    $.ajax({
        type: "POST",
        url: "/postProbSearch",
        data: JSON.stringify(data),
        dataType:'json' ,
        contentType: "application/json",
        success: function (response) {
            // if error has data => show error msg alert
            dom.dicInfoDetails.value = response.result;

            if (typeof(response.errors) != "undefined" && response.errors.length != 0 ) {
                alert((response.errors));
                dom.dicInfoDetails.value = response.errors;
            }
            // dom.dicInfoDetailsLeft.value = response.dicInfoLeft;
            //dom.dicInfoDetailsRight.value = response.dicInfoRight;
            // text.posTagged = response.result;
            // dom.dicInfoDetailsLeft.innerHTML = text.posTagged;

        }
    });
}



function postLexUpdate() {
    var data = {
        word : dom.lexWordInput.value,
        updateText : dom.lexDicInfoDetails.value
    };
    $.ajax({
        type: "POST",
        url: "/postLexUpdate",
        data: JSON.stringify(data),
        dataType:'json' ,
        contentType: "application/json",
        success: function (response) {
            // if error has data => show error msg alert
            alert(response.result)
            if (typeof(response.error) == 1) {
                alert((response.message));
                dom.dicInfoDetails.value = "";
            }
            // dom.dicInfoDetailsLeft.value = response.dicInfoLeft;
            //dom.dicInfoDetailsRight.value = response.dicInfoRight;
            // text.posTagged = response.result;
            // dom.dicInfoDetailsLeft.innerHTML = text.posTagged;

        }
    });
}

function postProbUpdate() {
    var data = {
        word : dom.probWordInput.value,
        updateText : dom.probDicInfoDetails.value
    };
    $.ajax({
        type: "POST",
        url: "/postProbUpdate",
        data: JSON.stringify(data),
        dataType:'json' ,
        contentType: "application/json",
        success: function (response) {
            // if error has data => show error msg alert
            alert(response.result)
            if (typeof(response.error) == 1) {
                alert((response.message));
                dom.dicInfoDetails.value = "";
            }
            // dom.dicInfoDetailsLeft.value = response.dicInfoLeft;
            //dom.dicInfoDetailsRight.value = response.dicInfoRight;
            // text.posTagged = response.result;
            // dom.dicInfoDetailsLeft.innerHTML = text.posTagged;

        }
    });
}

function postMakeLexicalDB() {

    $.ajax({
        type: "POST",
        url: "/postMakeLexicalDB",
        data: JSON.stringify({}),
        dataType:'json' ,
        contentType: "application/json",
        success: function (response) {
            // if error has data => show error msg alert
            dom.dicInfoDetails.value = response.result;
/*
            if (typeof(response.errors) != "undefined" && response.errors.length != 0 ) {
                alert((response.errors));
                dom.dicInfoDetails.value = response.errors;
            }
            // dom.dicInfoDetailsLeft.value = response.dicInfoLeft;
            //dom.dicInfoDetailsRight.value = response.dicInfoRight;
            // text.posTagged = response.result;
            // dom.dicInfoDetailsLeft.innerHTML = text.posTagged;
*/
        }
    });
}

function postMakeProbDB() {
    var data = {
        word : dom.wordInput.value,
        generics : dom.genericPOSInput.value,
        domains : dom.domainPOSInput.value
    };
    $.ajax({
        type: "POST",
        url: "/postMakeProbDB",
        data: JSON.stringify(data),
        dataType:'json' ,
        contentType: "application/json",
        success: function (response) {
            // if error has data => show error msg alert
            alert(response.result);
/*
            if (typeof(response.errors) != "undefined" && response.errors.length != 0 ) {
                alert((response.errors));
                dom.dicInfoDetails.value = response.errors;
            }
            // dom.dicInfoDetailsLeft.value = response.dicInfoLeft;
            //dom.dicInfoDetailsRight.value = response.dicInfoRight;
            // text.posTagged = response.result;
            // dom.dicInfoDetailsLeft.innerHTML = text.posTagged;
*/
        }
    });
}


