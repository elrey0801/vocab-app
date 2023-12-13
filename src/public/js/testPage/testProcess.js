const HOST = window.location.host.split(':')[0] == 'localhost' ? 'http://localhost:8888' : 'https://' + window.location.host; 
let checkTag = `<button id="submitBtn" type="button" class="btn btn-success" onclick="checkAnswer()">Check</button>`
let nextTag = `<button id="submitBtn" type="button" class="btn btn" onclick="nextQuestion()" style="background-color:rgb(20, 104, 152); color:white;">Next Question</button>`
let endTag = `<button id="submitBtn" type="button" class="btn btn" onclick="nextQuestion()" style="background-color:rgb(20, 104, 152); color:white;">End Test</button>`
document.getElementById('submitBtn').innerHTML = checkTag
var testData = JSON.parse(localStorage.getItem("testData"));
let currentQuestion = parseInt(localStorage.getItem("currentQuestion"));
console.log(currentQuestion);
if(!testData) window.location.href = HOST + "/vocab-set";
console.log(testData);
let numOfQuestion = testData.length;
if(currentQuestion === numOfQuestion) window.location.href = HOST + "/vocab-set";
let checkEle = null;

function getChoice() {
    let choiceGroup = document.getElementsByName('choice');
    for(let ans of choiceGroup)
        if(ans.checked)
            return ans.value
}
function clearChoice() {
    let choiceGroup = document.getElementsByName('choice');
    for(let ans of choiceGroup)
        if(ans.checked)
            return ans.checked = false
}

function updateScore(oldScore, newScore) {
    let diff = newScore - oldScore;
    if(diff >= 0)
        document.getElementById('questionFamiliarity').innerHTML = `<span style="color:green;">This word score: <b>${newScore} (+${diff})</b></span>`
    else
    document.getElementById('questionFamiliarity').innerHTML = `<span style="color:red;">This word score: <b>${newScore} (${diff})</b></span>`
}

function showAnswer(answer) {
    let choiceGroup = document.getElementsByName('choice');
    for(let ans of choiceGroup)
        if(ans.value === answer) {
            console.log(ans.value, answer);
            console.log(ans.id + '-label');
            checkEle = document.getElementById(ans.id + '-label');
            checkEle.classList.remove('btn-outline-primary');
            checkEle.classList.add('btn-success');
        }
            
}

async function checkAnswer() {
    let answer = getChoice();
    let familiarity = testData[currentQuestion].familiarity;
    let oldScore = familiarity;
    if(!answer) return;
    console.log(answer);
    showAnswer(testData[currentQuestion].meaning)
    if(answer === testData[currentQuestion].meaning) {
        if(familiarity < 5) familiarity += 2;
        else if(familiarity < 10) familiarity++;
    } else {
        if(familiarity > 5) familiarity -= 2;
        else if(familiarity > 0) familiarity--;
    }
    updateScore(oldScore, familiarity);


    const options = {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            vocabSetId: testData[currentQuestion].vocabSetId,
            word: testData[currentQuestion].word,
            meaning: testData[currentQuestion].meaning,
            example: testData[currentQuestion].example,
            familiarity:familiarity,
            id: testData[currentQuestion].id
        })
    };
    console.log(options);

    try {
        console.log(options);
        var response = await fetch(HOST + '/update-vocab', options);
        if(response.status == 201) console.log('Vocab is updated');
        else if(response.status == 422) {
            console.log('Validation Error');
        }
        else if(response.status == 401) window.location.href = HOST + "/login";
    } catch (e) {
        console.log(e);
    }
    currentQuestion++;
    localStorage.setItem("currentQuestion", currentQuestion);
    if (currentQuestion < numOfQuestion) 
        document.getElementById('submitBtn').innerHTML = nextTag
    else document.getElementById('submitBtn').innerHTML = endTag
}

function nextQuestion() {
    checkEle.classList.remove('btn-success');
    checkEle.classList.add('btn-outline-primary');
    if (currentQuestion < numOfQuestion) {
        showQuestion(currentQuestion);
    } else {
        localStorage.removeItem("testData");
        window.location.href = HOST + "/vocab-set";
    }
}

function showQuestion() {
    clearChoice();
    document.getElementById('submitBtn').innerHTML = checkTag
    let word = testData[currentQuestion].word;
    let example = testData[currentQuestion].example;
    let familiarity = testData[currentQuestion].familiarity;
    document.getElementById('questionNumber').innerHTML = `#${currentQuestion+1}/${numOfQuestion} question`
    document.getElementById('questionFamiliarity').innerHTML = `This word score: ${familiarity}`
    document.getElementById('questionWord').innerHTML = `Word: ${word}`
    document.getElementById('questionExample').innerHTML = `<i>Example: ${example ? example : '<b>No example provided</b>'}</i>`

    let choice1 = testData[currentQuestion].option[0];
    let choice2 = testData[currentQuestion].option[1];
    let choice3 = testData[currentQuestion].option[2];
    let choice4 = testData[currentQuestion].option[3];

    document.getElementById('choice-1-label').innerHTML = choice1
    document.getElementById('choice-2-label').innerHTML = choice2
    document.getElementById('choice-3-label').innerHTML = choice3
    document.getElementById('choice-4-label').innerHTML = choice4
    document.getElementById('choice-1').value = choice1
    document.getElementById('choice-2').value = choice2
    document.getElementById('choice-3').value = choice3
    document.getElementById('choice-4').value = choice4
}

function showResult() {
    
}

function getTheTest() {
    
}
showQuestion(currentQuestion);