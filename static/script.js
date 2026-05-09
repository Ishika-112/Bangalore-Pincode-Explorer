async function searchArea() {

    const area = document.getElementById("areaInput").value;

    const response = await fetch(`/search/area/${area}`);

    const data = await response.json();

    if(data.pincode){
        document.getElementById("areaResult").innerText =
            `Pincode: ${data.pincode}`;
    }else{
        document.getElementById("areaResult").innerText =
            data.message;
    }
}


async function searchPincode() {

    const pincode = document.getElementById("pincodeInput").value;

    const response = await fetch(`/search/pincode/${pincode}`);

    const data = await response.json();

    if(data.area){
        document.getElementById("pincodeResult").innerText =
            `Area: ${data.area}`;
    }else{
        document.getElementById("pincodeResult").innerText =
            data.message;
    }
}