CONTACT_DETAIL = """
    <div class="container">
        <form class="row g-3">
            <div class="col-sm-12">
                <label for="inputEmail4" class="form-label">Email Adresinizi Giriniz</label>
                <input type="email" class="form-control" id="inputEmail4">
            </div>
            <div class="col-sm-12">
                <label for="exampleFormControlTextarea1" class="form-label">Açıklama</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
              </div>
            <div class="col-sm-12">
                <label for="inputState" class="form-label">Bize Nasıl Ulaştınız?</label>
                <select id="inputState" class="form-select">
                    <option selected>Seçiniz</option>
                    <option>Sosyal Medya</option>
                    <option>Google</option>
                    <option>Referans</option>
                    <option>Arkadaş Tavsiyesi</option>
                </select>
            </div>
            <div class="col-12">
                <button type="submit" class="btn btn-primary">Gönder</button>
            </div>
        </form>
    </div>
"""

ABOUT_US_DETAIL = """<div class="container">
  <div class="row">
    <div class="col-sm-12">
      <h2 class="text-center">
        Vizyonumuz
      </h2>
      <hr>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. At provident ea possimus ratione dicta
        exercitationem deserunt tempore, id obcaecati ipsa?</p>
      <ul>
        <li>Lorem, ipsum.</li>
        <li>Laudantium, dicta.</li>
        <li>Sapiente, nobis?</li>
        <li>Repudiandae, nobis!</li>
        <li>Ipsum, quia!</li>
      </ul>
    </div>
    <div class="col-sm-12">
      <h2 class="text-center">
        Misyonumuz
      </h2>
      <hr>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. At provident ea possimus ratione dicta
        exercitationem deserunt tempore, id obcaecati ipsa?</p>
      <ul>
        <li>Lorem, ipsum.</li>
        <li>Laudantium, dicta.</li>
        <li>Sapiente, nobis?</li>
        <li>Repudiandae, nobis!</li>
        <li>Ipsum, quia!</li>
      </ul>
    </div>
  </div>
</div>"""

VİSİON_DETAIL = """  <div class="container">
    <div class="row">
      <div class="col-sm-12">
      <h2 class="text-center">
        Vizyonumuz
      </h2>
      <hr>
      <p class="text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit. At provident ea possimus ratione dicta exercitationem deserunt tempore, id obcaecati ipsa?</p>
      <p class="text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit. At provident ea possimus ratione dicta exercitationem deserunt tempore, id obcaecati ipsa?</p>
      <p class="text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit. At provident ea possimus ratione dicta exercitationem deserunt tempore, id obcaecati ipsa?</p>
      <p class="text-center">Lorem ipsum dolor sit amet consectetur adipisicing elit. At provident ea possimus ratione dicta exercitationem deserunt tempore, id obcaecati ipsa?</p>
        <ul clas="d">
          <li>Lorem, ipsum.</li>
          <li>Laudantium, dicta.</li>
          <li>Sapiente, nobis?</li>
          <li>Repudiandae, nobis!</li>
          <li>Ipsum, quia!</li>
        </ul>
      </div>
     </div>
  </div>"""

FAKE_DB_PAGES = [
  {"url" : "iletisim" , "detail": CONTACT_DETAIL, "title" : "İletisim"},  
  {"url" : "hakkimizda" , "detail": ABOUT_US_DETAIL, "title": "Hakkimizda"},  
  {"url" : "vizyonumuz" , "detail": VİSİON_DETAIL, "title": "Vizyonumuz"},  
]
