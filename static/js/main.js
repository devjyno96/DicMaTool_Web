let dom = {
    wordInput : null,
    genericPOSInput : null,
    domainPOSInput : null,
    searchButton : null,
    clearButton : null,

    updateButton : null,
    makeGenericDBButton : null,
    makeDomainDBButton : null,

    dicInfoDetailsLeft : null,
    dicInfoDetailsRight : null,
    dicInfoDetails : null
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
    dom.wordInput = document.getElementById("wordInput");
    dom.genericPOSInput = document.getElementById("genericPOSInput");
    dom.domainPOSInput = document.getElementById("domainPOSInput");
    dom.searchButton = document.getElementById("searchButton");
    dom.clearButton = document.getElementById("clearButton");
    // dom.dicInfoDetailsLeft = document.getElementById("dicInfoDetailsLeft");
    // dom.dicInfoDetailsRight = document.getElementById("dicInfoDetailsRight");
    dom.dicInfoDetails = document.getElementById("dicInfoDetails");
    dom.updateButton = document.getElementById("updateButton");
    dom.makeGenericDBButton = document.getElementById("MakeGenericButton");
    dom.makeDomainDBButton = document.getElementById("MakeDomainButton");
}

/**
 * 이벤트 리스너를 등록한다.
 */
function registerListeners() {
    dom.searchButton.addEventListener("click", onSearchButtonClick);
    dom.clearButton.addEventListener("click", onClearButtonClick);
    dom.updateButton.addEventListener("click", onUpdateButtonClick);
}
// input values initialize
function onClearButtonClick(){
    dom.wordInput.value = null;
    dom.genericPOSInput.value = null;
    dom.domainPOSInput.value = null;
    // dom.dicInfoDetailsLeft.value = null;
    // dom.dicInfoDetailsRight.value = null;
    dom.dicInfoDetails.value = null;
}
//search Button Event
function onSearchButtonClick(){
    requestPosTag();
}
//search Button Event
function onUpdateButtonClick(){
    requestMakeGenericDB();
}

//Post function
//post - word, generic, domain
//response - dicInfoLeft, Right
function requestPosTag() {
    var data = {
        word : dom.wordInput.value,
        generics : dom.genericPOSInput.value,
        domains : dom.domainPOSInput.value
    };

    $.ajax({
        type: "POST",
        url: "/postSearch",
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

function requestMakeGenericDB() {

    $.ajax({
        type: "POST",
        url: "/postMakeGenericDB",
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


