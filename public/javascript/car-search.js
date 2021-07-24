async function onPageLoad() {
    try {
        hideLoadingDiv()
        showContentPanel()
    } catch (err) {
        console.log(err)
    }
}

function validateForm() {

    let carName = document.getElementById("carName").value;

    if(carName === "") {
        alert('Name not valid');
    }

    return carName.toLowerCase().replace(/[^\w\s]/gi, '')
}

async function validateSearchAndRender(isExact){

    let carNameQuery = validateForm()

    let allCarsArray = await getCarsData(carNameQuery, isExact)

    if (allCarsArray.length === 0) {
        alert('No results found, please try again');
        throw new Error("No Results")
    }

    renderFilesAndS3links(allCarsArray)
}

function renderFilesAndS3links(allCarsArray){

    document.getElementById("tableBody").innerHTML ='';
    document.getElementsByTagName("FORM")[0].reset();

    allCarsArray.forEach(function(item){
        let individualItemRow =
         `<tr>
            <td class="title">${item.Name}</td>
            <td class="title">${item.Miles_per_Gallon}</td>
            <td class="title">${item.Cylinders}</td>
            <td class="title">${item.Displacement}</td>
            <td class="title">${item.Horsepower}</td>
            <td class="title">${item.Weight_in_lbs}</td>
            <td class="title">${item.Acceleration}</td>
            <td class="title">${item.Year}</td>
            <td class="title">${item.Origin}</td>
         </tr>` ;

        document.getElementById("tableBody").innerHTML += individualItemRow
    });

    document.getElementById('tableOverflow').classList.remove('d-none');
}

function hideLoadingDiv(){
    document.getElementById('loadingDiv').classList.add('d-none');
}

function showContentPanel() {
    document.getElementById('manageS3ContentPanel').classList.remove('d-none');
}

document.addEventListener("DOMContentLoaded", function(){
    onPageLoad();
});

