const HOST = window.location.host.split(':')[0] == 'localhost' ? 'http://localhost:8888' : 'https://' + window.location.host; 
group = document.querySelector('#list-group');
async function getVocabSetList() {
    const options = {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
    };
    try {
        console.log(options);
        var response = await fetch(HOST + '/get-vocabsets', options);
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
                                <a href="${HOST + '/vocabs/' + res.id}" type="button" class="d-flex gap-2 w-100 align-items-center" style="text-decoration: none; color:black;">
                                    <h6 class="mb-0 fw-bold" vocabSetName="${res.vocabSetName}" vocabSetId="${res.id}">${res.vocabSetName}</h6>
                                </a>
                                <div class="btn-group" role="group" aria-label="Basic example">
                                    <button type="button" class="btn btn-outline-info" data-bs-toggle="modal" data-bs-target="#createTestModal" vocabSetName="${res.vocabSetName}" vocabSetId="${res.id}">Practice</button>
                                    <button type="button" class="btn btn-outline-success" data-bs-toggle="modal" data-bs-target="#changeVocabSetNameModal" vocabSetName="${res.vocabSetName}" vocabSetId="${res.id}">Edit</button>
                                    <button class="btn btn-outline-danger" data-bs-toggle="modal" data-bs-target="#deleteVocabSetModal" vocabSetId="${res.id}" vocabSetName="${res.vocabSetName}" type="button">Delete</button>
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
getVocabSetList();

async function changeVocabSetName() {
    var data = document.querySelector('.modal-body #vocabSetNewName')
    var vocabSetId = parseInt(data.getAttribute('vocabSetId'))
    var vocabSetNewName = data.value
    const options = {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            vocabSetName: vocabSetNewName, 
            id: vocabSetId
        })
    };

    try {
        console.log(options);
        var response = await fetch(HOST + '/update-vocabset', options);
        if(response.status == 201) console.log('VocabSet name is changed');
        else if(response.status == 422) {
            console.log('Validation Error');
        }
        else if(response.status == 401) window.location.href = HOST + "/login";
        var changeVocabSetNameModal = bootstrap.Modal.getInstance(document.getElementById('changeVocabSetNameModal'))
        changeVocabSetNameModal.hide()
    } catch (e) {
        console.log(e);
    }
    getVocabSetList();
}

async function deleteVocabSet(vocabSetId) {
    const options = {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            id: parseInt(document.getElementById('deleteVocabSetModal').getAttribute('vocabSetId'))
        })
    };
    try {
        console.log(options);
        var response = await fetch(HOST + '/delete-vocabset', options);
        if(response.status == 202) console.log('VocabSet is deleted');
        else if(response.status == 422) {
            console.log('Validation Error');
        }
        else if(response.status == 401) window.location.href = HOST + "/login";
    } catch (e) {
        console.log(e);
    }
    getVocabSetList();
}

async function createNewVocabSet() {
    var data = document.querySelector('.modal-body #createVocabSet')
    var vocabSetName = data.value
    const options = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            vocabSetName: vocabSetName, 
        })
    };

    try {
        console.log(options);
        var response = await fetch(HOST + '/post-vocabset', options);
        if(response.status == 201) console.log('VocabSet created');
        else if(response.status == 422) {
            console.log('Validation Error');
        }
        else if(response.status == 401) window.location.href = HOST + "/login";
        var createNewVocabSetModal = bootstrap.Modal.getInstance(document.getElementById('createNewVocabSetModal'))
        createNewVocabSetModal.hide()
        data.value = ''
    } catch (e) {
        console.log(e);
    }
    getVocabSetList();
}