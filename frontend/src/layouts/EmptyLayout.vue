<template>
  <section class="vh-100 bg-image" id="random" style="background-size: 100%;">
    <div class="mask d-flex align-items-center h-100 gradient-custom-3">
      <div class="container h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <router-view />
        </div>
      </div>
    </div>
  </section>
</template>


<script>
  /**
   * Ставит рандомную картинку на фон
   */
  document.addEventListener("DOMContentLoaded", function() {
    const image_urls = [
      "url('https://img.freepik.com/free-photo/river-surrounded-by-forests-under-a-cloudy-sky-in-thuringia-in-germany_181624-30863.jpg?w=996&t=st=1652216511~exp=1652217111~hmac=8896cc8502dfa9a69639370eb2f4b7c7daa3954c5ad8dd4bbd96b450c4e41697')",
      "url('https://images.pexels.com/photos/3244513/pexels-photo-3244513.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=1920&w=1321')",
      "url('https://images.pexels.com/photos/15286/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)",
      "url('https://images.pexels.com/photos/572897/pexels-photo-572897.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)",
      "url('https://images.pexels.com/photos/3293148/pexels-photo-3293148.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)",
      "url('https://images.pexels.com/photos/3509971/pexels-photo-3509971.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)",
      "url('https://images.pexels.com/photos/4534200/pexels-photo-4534200.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)",
      "url('https://images.pexels.com/photos/4101555/pexels-photo-4101555.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)",
      "url('https://images.pexels.com/photos/924824/pexels-photo-924824.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)",
      "url('https://images.pexels.com/photos/2387873/pexels-photo-2387873.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)",

    ];
    const random = Math.floor(Math.random() * image_urls.length);
    document.getElementById("random").style.backgroundImage=image_urls[random];
  });
</script>