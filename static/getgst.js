console.log("hii");
let filtered_gst_data = null;

function prepare_item_card(
  index,
  hsn = "-",
  desc = "-",
  cgst = "-",
  sgst = "-",
  igst = "-",
  cess = "-"
) {
  return `
        <div class="card">
            <div class="info">
                <div class="code">
                    <p>code:</p>
                    <p>${hsn}</p>
                </div>
                <div class="desc">
                    <p>desccription:</p>
                    <p>${desc}</p>
                </div>
            </div>
            <div class="gst">
                <div class="cgst">
                    <p>CGST:</p>
                    <p>${cgst}</p>
                </div>
                <div class="sgst">
                    <p>SGST:</p>
                    <p>${sgst}</p>
                </div>
                <div class="igst">
                    <p>IGST:</p>
                    <p>${igst}</p>
                </div>
                <div class="cess">
                    <p>Cess:</p>
                    <p>${cess}</p>
                </div>
            </div>
            <div class="slide">
            <div  onclick="set_selected_gst(${index})">Select</div>
            </div>
        </div>`;
}

async function get_filtered_gst_data() {
  let query = document.getElementById("input_product_data").value;
  let options_div = document.getElementById("options");
  document.getElementById("selected_gst").style.display = "none";
  document.getElementById("filtered_data").style.display = "block";

  filtered_gst_data = await fetch(`/filter_gst/${query}`)
    .then((res) => res.json())
    .then((data) => data);
  options_div.innerHTML = "";
  if (filtered_gst_data.length) {
    filtered_gst_data.map((data, index) => {
      let card = prepare_item_card(
        index,
        data.fields.hsn,
        data.fields.desc,
        data.fields.cgst,
        data.fields.sgst,
        data.fields.igst,
        data.fields.cess
      );

      options_div.innerHTML += card;
    });
  } else {
    options_div.innerHTML +=
      "Results not found. Try using alternatives based on guidelines.";
  }
}
document
  .getElementById("input_product_data")
  .addEventListener("keypress", (e) => {
    if (e.key == "Enter") get_filtered_gst_data();
  });

function set_selected_gst(index) {
  selected_item = filtered_gst_data[index];
  document.getElementById("code").value = selected_item.fields.hsn;
  document.getElementById("desc").value = selected_item.fields.desc;
  document.getElementById("cgst").value = selected_item.fields.cgst;
  document.getElementById("sgst").value = selected_item.fields.sgst;
  document.getElementById("igst").value = selected_item.fields.igst;
  document.getElementById("cess").value = selected_item.fields.cess;
  document.getElementById("filtered_data").style.display = "none";
  document.getElementById("set_gst").style.display = "none";
  document.getElementById("selected_gst").style.display = "block";
}
