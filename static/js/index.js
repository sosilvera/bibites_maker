const apiUrl = "http://127.0.0.1:30095/sims";
const t3_button = document.getElementById("t3");

async function getSistemByURL(){
    try{
        var url = window.location.href;
        console.log(url)
    } catch (error){
        console.error("Error al obtener SIM:", error);
    }
}

async function getSim(sistema){
    try{
        const response = await fetch(`${apiUrl}/getSim/${sistema}`);
        const data = await response.json();
        console.log(data["iccId"]);
    } catch (error){
        console.error("Error al obtener SIM:", error);
    }
}

async function showModal(){
    console.log("Mostrar modal")
}

async function cancelLock(iccId){
    console.log("Cancelo el lock")
}