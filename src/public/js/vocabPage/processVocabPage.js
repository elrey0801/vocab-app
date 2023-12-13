const HOST = window.location.host.split(':')[0] == 'localhost' ? 'http://localhost:8888' : 'https://' + window.location.host; 
group = document.querySelector('#list-group');
vocabSetId = document.querySelector('body').getAttribute('vocabSetId');
async function getVocabList() {
    try {
        var response = await fetch(HOST + `/get-vocabs/${vocabSetId}`);
        if(response.status == 200) {
            response = await response.json();
            console.log(response);
            var element = "";
            for(var res of response) {
                element += `
                <div class="container">
                    <div class="row py-2 justify-content-center align-items-center">
                        <div class="list-group col-lg-9 d-flex">
                            <div class="list-group-item list-group-item-action d-flex gap-3 py-3" aria-current="true">
                                <img src="${HOST + '/public/img/logo.png'}" alt="twbs" width="32" height="32" class="rounded-circle flex-shrink-0">
                                <div class="d-flex gap-2 w-100 align-items-center" data-bs-toggle="modal" data-bs-target="#vocabModal" vocabWord="${res.word}" vocabMeaning="${res.meaning}" vocabExample="${res.example ? res.example : ""}" vocabFamiliarity="${res.familiarity}">
                                    <h6 class="mb-0 fw-bold" vocabId="${res.id}">${res.word}</h6>
                                </div>
                                <div class="btn-group" role="group" aria-label="Basic example">
                                    <button type="button" class="btn btn-outline-success"  data-bs-toggle="modal" data-bs-target="#changeVocabModal" vocabWord="${res.word}" vocabMeaning="${res.meaning}" vocabExample="${res.example ? res.example : ""}" vocabFamiliarity="${res.familiarity}" vocabId="${res.id}">Edit</button>
                                    <button class="btn btn-outline-danger" data-bs-toggle="modal" data-bs-target="#deleteVocabModal" vocabId="${res.id}" vocabWord="${res.word}" vocabMeaning="${res.meaning}" vocabExample="${res.example ? res.example : ""}" type="button">Delete</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>`
            }
            group.innerHTML = element;
        }
        else if(response.status == 422) {
            console.log('Validation Error');
        }
        else if(response.status == 401) window.location.href = HOST + "/login";
    } catch (e) {
        console.log(e);
    }
}
getVocabList();

async function changeVocab() {
    const options = {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            vocabSetId: document.querySelector('body').getAttribute('vocabSetId'),
            word: document.querySelector('.modal-body #changeVocabModal-vocabWord').value,
            meaning: document.querySelector('.modal-body #changeVocabModal-vocabMeaning').value,
            example: document.querySelector('.modal-body #changeVocabModal-vocabExample').value,
            familiarity: parseInt(document.getElementById('changeVocabModal').getAttribute('vocabFamiliarity')),
            id: parseInt(document.getElementById('changeVocabModal').getAttribute('vocabId'))
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
        bootstrap.Modal.getInstance(document.getElementById('changeVocabModal')).hide()
    } catch (e) {
        console.log(e);
    }
    getVocabList();
}

async function deleteVocab() {
    const options = {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            id: parseInt(document.getElementById('deleteVocabModal').getAttribute('vocabId')),
            vocabSetId: parseInt(document.querySelector('body').getAttribute('vocabSetId'))
        })
    };
    console.log(options);
    try {
        console.log(options);
        var response = await fetch(HOST + '/delete-vocab', options);
        if(response.status == 202) console.log('Vocab is deleted');
        else if(response.status == 422) {
            console.log('Validation Error');
        }
        else if(response.status == 401) window.location.href = HOST + "/login";
    } catch (e) {
        console.log(e);
    }
    getVocabList();
}

async function createVocab() {
    const options = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            vocabSetId: document.querySelector('body').getAttribute('vocabSetId'),
            word: document.querySelector('.modal-body #createVocabModal-vocabWord').value,
            meaning: document.querySelector('.modal-body #createVocabModal-vocabMeaning').value,
            example: document.querySelector('.modal-body #createVocabModal-vocabExample').value,
        })
    };

    try {
        console.log(options);
        var response = await fetch(HOST + '/post-vocab', options);
        if(response.status == 201) console.log('Vocab created');
        else if(response.status == 422) {
            console.log('Validation Error');
        }
        else if(response.status == 401) window.location.href = HOST + "/login";
        bootstrap.Modal.getInstance(document.getElementById('createVocabModal')).hide()
        document.querySelector('.modal-body #createVocabModal-vocabWord').value = ''
        document.querySelector('.modal-body #createVocabModal-vocabMeaning').value = ''
        document.querySelector('.modal-body #createVocabModal-vocabExample').value = ''
    } catch (e) {
        console.log(e);
    }
    getVocabList();
}
