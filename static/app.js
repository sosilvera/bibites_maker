// Ejecuta al cargar la página
window.onload = async () => {
  const res = await fetch("/bibites/list");
  const data = await res.json();

  const select = document.getElementById("file");
  if (!data.files.length) {
    select.innerHTML = `<option>No se encontraron archivos .bb8template</option>`;
    return;
  }

  select.innerHTML = data.files.map(f => `<option>${f}</option>`).join("");
};

// Procesar con backend
document.getElementById("processBtn").addEventListener("click", async () => {
  const file = document.getElementById("file").value;
  const instructions = document.getElementById("instructions").value;
  const btn = document.getElementById("processBtn");

  if (!file || !instructions) {
    alert("Completa todos los campos.");
    return;
  }

  btn.disabled = true;
  btn.innerHTML = `<span class="spinner"></span> Procesando...`;

  try {
    const res = await fetch("/bibites/process", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ file, instructions })
    });

    if (!res.ok) throw new Error("Error del servidor");

    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = file.replace(".bb8template", "_nuevo.bb8template");
    document.body.appendChild(a);
    a.click();
    a.remove();
    window.URL.revokeObjectURL(url);

  } catch (err) {
    alert("Error procesando el Bibite: " + err.message);
  } finally {
    btn.disabled = false;
    btn.innerHTML = "Procesar y Descargar Bibite";
  }
});
