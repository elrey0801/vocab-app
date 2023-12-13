// reference: https://getbootstrap.com/docs/5.0/components/modal/
// for creating a test
var createTestModal = document.getElementById('createTestModal')
createTestModal.addEventListener('show.bs.modal', async function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget

    var vocabSetName = button.getAttribute('vocabSetName')
    var vocabSetId = button.getAttribute('vocabSetId')

    var modalTitle = createTestModal.querySelector('.modal-title')
    modalTitle.innerHTML = 'Practice VocabSet <br>@' + vocabSetName

    
    var maxNumOfVocabs = await getTestInfo(vocabSetId);
    createTestModal.querySelector('.modal-body #createTest-numOfVocabs').value = maxNumOfVocabs < 20 ? maxNumOfVocabs : 20;
    
    createTestModal.querySelector('.modal-body #createTest-numOfVocabs-label').innerHTML = `Number of vocabs <b>(you have ${maxNumOfVocabs} vocab(s))</b>: `

    createTestModal.setAttribute('vocabSetId', vocabSetId)
    createTestModal.setAttribute('maxNumOfVocabs', maxNumOfVocabs)
})


async function getTestInfo(vocabSetId) {
    const HOST = window.location.host.split(':')[0] == 'localhost' ? 'http://localhost:8888' : 'https://' + window.location.host; 
    try {
        var response = await fetch(HOST + '/get-vocabs/' + vocabSetId);
        if(response.status == 200) {
            response = await response.json();
            return response.length;
        }
        else if(response.status == 422) {
            console.log('Validation Error');
        }
        else if(response.status == 401) window.location.href = HOST + "/login";
    } catch (e) {
        console.log(e);
    }
}

async function createTest() {
    var createTestModal = document.getElementById('createTestModal');
    var vocabSetId = parseInt(createTestModal.getAttribute('vocabSetId'));
    var maxNumOfVocabs = parseInt(createTestModal.getAttribute('maxNumOfVocabs'));
    var numOfVocabs = parseInt(createTestModal.querySelector('.modal-body #createTest-numOfVocabs').value);

    if(maxNumOfVocabs < 5) {
        errorStr = 'You have to have at least 5 vocabs to create a test';
        createTestModal.querySelector('.modal-body #createTest-warning-label').innerHTML = errorStr
        return;
    }
    if(numOfVocabs < 5) {
        errorStr = 'You have to set at least 5 vocabs to create a test';
        createTestModal.querySelector('.modal-body #createTest-warning-label').innerHTML = errorStr
        return;
    }
    if(numOfVocabs > 20) {
        errorStr = 'Maximum vocabs for a test is 20';
        createTestModal.querySelector('.modal-body #createTest-warning-label').innerHTML = errorStr
        return;
    }
    if(numOfVocabs > maxNumOfVocabs) {
        errorStr = `You only have ${maxNumOfVocabs} vocabs`;
        createTestModal.querySelector('.modal-body #createTest-warning-label').innerHTML = errorStr
        return;
    }
    
    const options = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            vocabSetId: vocabSetId, 
            numOfVocabs: numOfVocabs
        })
    };

    try {
        console.log(options);
        var response = await fetch(HOST + '/get-test', options);
        if(response.status == 200) {
            response = await response.json();
            localStorage.setItem("testData", JSON.stringify(response));
            localStorage.setItem("currentQuestion", 0);
            createTestModal.querySelector('.modal-body #createTest-warning-label').innerHTML = ''
            window.location.href = HOST + "/test"
        }
        else if(response.status == 422) {
            console.log('Validation Error');
        }
        else if(response.status == 401) window.location.href = HOST + "/login";
    } catch (e) {
        console.log(e);
        errorStr = `Error when getting test, please try again`;
        createTestModal.querySelector('.modal-body #createTest-warning-label').innerHTML = errorStr
    }
}
