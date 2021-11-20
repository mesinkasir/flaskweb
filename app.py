from flask import Flask, render_template
app = Flask(__name__)

content = [
    {
        'title': 'Pembuatan Aplikasi Android',
        'cover': 'https://1.bp.blogspot.com/-WzqU0S3J3HI/YLfSK7OiiEI/AAAAAAAAOz0/MG5agWdHE3UeHlDJUX2bpmrcUKhMgf9wgCLcBGAsYHQ/s1875/71828746_10215543827769756_8559723998198366208_n.jpg',
        'description': 'Dan saat nya kini menggunakan layanan jasa pembuatan aplikasi android untuk informasi usaha dan bisnis mu, dengan memiliki aplikasi android apk sendiri tentunya akan membantu untuk semakin dekat dengan pelanggan, dengan memiliki apk android ini sendiri kamu bisa juga bisa upload ke google playstore dengan account developer kamu, dengan ini maka lebih bebas untuk memberikan keterangan mengenai apk android mu di google playstore. Atau kamu juga bisa menggunakan layanan bantuan untuk upload app bundle kamu ke playstore jika dibutuhkan.',
        'button': 'Get Start Now',
        'link': './about/',
        'section1title' : 'Aplikasi Android Flutter Ionic React Native',
        'section1': 'Custom - menggunakan technology terbaru dengan dukungan flutter,react native ionic untuk proses develope aplikasi android mu.',
        'cover1': 'https://1.bp.blogspot.com/-aTwNVRDBHv8/YLcDvFCQH4I/AAAAAAAAOWg/fl1Oj8lhlqQsOY-994SQdrSUUtkO39pPQCLcBGAsYHQ/s960/12042681_10205005324793768_1811671595756355728_n.jpg',
        'section1Url': '/flutter-ionic-react/',
        'section1content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section2title' : 'Aplikasi Android Native',
        'section2': 'Native - solusi terbaik dengan native java maupun kotlin untuk menghasilkan aplikasi bundle yang super ringan dan kecil.',
        'section2content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section2Url' : '/native/',
        'cover2': 'https://1.bp.blogspot.com/-hAN6-_VAiOI/YLcD1z1UBII/AAAAAAAAOX0/VrV0OUYsjJoFRFY1um_eREa7iw_YLGKxwCLcBGAsYHQ/s960/14203138_10207228936942682_3597044987583593770_n.jpg',
        'section4title': 'Website Applikasi Android',
        'section4content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section4': 'Web App - integrasikan dengan website dan aplikasi baik dalam bekerja point of sale , website informasi dan android app mu.',
        'cover4': 'https://1.bp.blogspot.com/-Ob9lOX5E5Ts/YLcDutk0CUI/AAAAAAAAOWc/2WkkcIv8psMH2Gl5co6UvRXFoTeBunfoQCLcBGAsYHQ/s960/11230651_10204870702508295_7974037716692577327_n.jpg',
        'section4Url' : '/webapp/',
        'section5title' : 'Pembuatan aplikasi android webview',
        'section5Url' : '/webview/',
        'section5content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section5': 'Webview - solusi termurah untuk kebutuhan mengkonvert website mu menjadi sebuah apk bundle android apps.',
        'cover5': 'https://1.bp.blogspot.com/-HCNazywWFPM/YLcDueKRjDI/AAAAAAAAOWU/9s5Zx8e9ySQZwaktdSxRfqK07qpPHuDdQCLcBGAsYHQ/s960/11130160_10203968824241902_1704446697852246306_n%2B-%2BCopy.jpg',
        'section6title' : 'Buat aplikasi android dengan single page apps',
        'section6content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section6': 'Single Page App - Kembangkan dengan angular ,react dan svelte untuk all in one website dan android app dalam satu.',
        'cover6': 'https://1.bp.blogspot.com/-G6Ig3TDAMU4/YLcDxzISnoI/AAAAAAAAOXA/-IH8DX9esVUSvQzqP0vZpUr6tkSjClYggCLcBGAsYHQ/s960/13406805_10206589188349367_938707191884813742_n.jpg',
        'section7title' : 'Pembuatan aplikasi android sekolah',
        'section7content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section7': 'Kebutuhan sekolah semakin mudah dengan school android apps untuk digunakan',
        'cover7': 'https://1.bp.blogspot.com/-n5bp--fnEBU/YLcDx4H7WYI/AAAAAAAAOXE/JIgpF9dQUxIoDrF6miB9Dgi8gkP0etglACLcBGAsYHQ/s960/13419272_10206645140588138_2543166287042910822_n.jpg',
        'section8': 'Untuk toko shop dengan kebutuhan informasi dan shortcut link ke toko online shop',
        'cover8': 'https://1.bp.blogspot.com/-qH9SUHsPPFA/YLcDymYc6DI/AAAAAAAAOXI/b1jX3V9dtQoYjYsX98sJJOvbmanc7Vu9wCLcBGAsYHQ/s960/13507054_10206713718662547_6644315528859008093_n.jpg',
        'section9': 'Special untuk restoran cafe rumah makan semakin memudahkan pelanggan untuk cek menu',
        'cover9': 'https://1.bp.blogspot.com/-A_NlLCSEs90/YLfR9k56TyI/AAAAAAAAOxk/X6j-0EqQJikkKUjuyCWXOSHHxWchijKmACLcBGAsYHQ/s2048/23415535_10210768584791666_6275021180249258681_o.jpg',
        'section10': 'Company profile perusahaan pastinya akan membutuhkan icon pada google playstore',
        'cover10': 'https://1.bp.blogspot.com/-RGC3u1jiELA/YLfSICF1VSI/AAAAAAAAOzU/n6B1ebgIq54FrV_nn8tNva3589QlHHQugCLcBGAsYHQ/s2048/49608166_10213717839081180_4982751856859021312_n.jpg',
        'section11': 'Untuk salon spa , hotel dengan kebutuhan booking online integrasi website langsung.',
        'cover11': 'https://1.bp.blogspot.com/-Tld34TGFrXU/YLfR4MwDGQI/AAAAAAAAOws/WknQo-SB9l8qIp7id74BBHDuybDH3owHQCLcBGAsYHQ/s960/12803080_10205997738283485_6444993107678205190_n.jpg',
        'section12': 'Bagi pekerja seni dengan gallery karya nya untuk ditampilkan via android apps.',
        'cover12': 'https://1.bp.blogspot.com/-3FM3secOOc4/YLfR-hsvEQI/AAAAAAAAOxs/tlk8-2X-O0wT8aIUyEdq_mzya_cVCc10wCLcBGAsYHQ/s2048/25734257_10211062510699630_6028128390988426982_o.jpg',
        'section6Url' : '/pwa/',
        'section7Url' : '/androidsekolah/',
        'section8Url' : '/toko/',
        'section9Url' : '/resto/',
        'section10Url' : '/company/',
        'section11Url' : '/booking/',
        'section12Url' : '/artwork/',
        'section8title' : 'Aplikasi android untuk toko shop outlet mu',
        'section8content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section9title' : 'Aplikasi android restoran cafe rumah makan.',
        'section9content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section10title' : 'Pembuatan Aplikasi dan website company profile',
        'section10content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section11title' : 'Aplikasi untuk salon spa, hotel dengan kebutuhan booking system',
        'section11content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
        'section12title' : 'Pembuatan Aplikasi android gallery seni',
        'section12content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
    }
]
aboutu = [
    {
        'title': 'Seberapa penting nya memiliki aplikasi Android',
        'Url': '/about/',
        'cover': 'https://1.bp.blogspot.com/-gIg6k1B79Zo/YLfR6jtTGqI/AAAAAAAAOxI/pPLKpOv8RrIugerQ9fejfmjixHkDJEzwQCLcBGAsYHQ/s2048/15138409_10207879409764096_2174835022262532037_o.jpg',
        'description': 'Mengapa kita butuh memiliki aplikasi android apa fungsi dan tujuan nya sendiri kita akan ulas disini.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'content1': 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
    }
]
prices = [
    {
        'title': 'Daftar harga layanan pembuatan aplikasi android',
        'Url': '/pricing/',
        'cover1': 'https://start.axcora.com/img/themesas.png',
        'price1': 'Rp.1.000.000',
        'fitur1': 'Aplikasi android bundle native java tech dengan standard design , dengan 5 halaman fitur(belum termasuk upload playstore google) + upload playstore hanya Rp.350.000',
        'title1': 'Murah',
        'url1': 'https://wa.me/6285646104747?text=Axcorasapps%20saya%20mau%20order%20Android App%0ANama/Shop%20%3A%0AAlamat%20%3A%0APaketwebapp%20%3AAPlikasiandroid-murah%0APrice%20%3ARp.1.000.000%0APembayaran%20via%20%3A%0ABCA%20181884109%20Suci%20Chanifah%0A%0Atolong%20diproses%20pesanan%20saya',
        'cover2': 'https://start.axcora.com/img/3.png',
        'price2': 'Rp.1.500.000',
        'fitur2': 'Aplikasi android bundle native java / flutter tech dengan premium design , dengan 5 halaman fitur(belum termasuk upload playstore google) + upload playstore hanya Rp.350.000',
        'title2': 'Premium',
        'url2': 'https://wa.me/6285646104747?text=Axcorasapps%20saya%20mau%20order%20Android App%0ANama/Shop%20%3A%0AAlamat%20%3A%0APaketwebapp%20%3AAPlikasiandroid-murah%0APrice%20%3ARp.1.500.000%0APembayaran%20via%20%3A%0ABCA%20181884109%20Suci%20Chanifah%0A%0Atolong%20diproses%20pesanan%20saya',
        'cover3': 'https://start.axcora.com/img/1.png',
        'price3': 'Rp.2.500.000',
        'fitur3': 'Modern website single page application + aplikasi android bundle apps, dengan fitur 5 halaman (belum termasuk upload playstore google) + upload playstore hanya Rp.350.000 dan perpanjangan website hanya Rp.600.000/tahun jika ingin aktivkan website modern pertahun,untuk apk sekali order',
        'title3': 'All in',
        'url3': 'https://wa.me/6285646104747?text=Axcorasapps%20saya%20mau%20order%20Android App%0ANama/Shop%20%3A%0AAlamat%20%3A%0APaketwebapp%20%3AAPlikasiandroid-murah%0APrice%20%3ARp.2.500.000%0APembayaran%20via%20%3A%0ABCA%20181884109%20Suci%20Chanifah%0A%0Atolong%20diproses%20pesanan%20saya',
        'fitur4': 'Convert website menjadi apk hanya Rp.350.000 bundle app android (belum termasuk upload google playstore)',
        'fitur5': 'Tambahan Halaman android apps Rp.250.000/page',
        'title4': 'Layanan lain',
        'cover4': 'https://1.bp.blogspot.com/-XSZbHxN1Poc/YLfR6QRh-DI/AAAAAAAAOxE/hgCfdFXQplkBgYUMYOsQK3Xc6mSaH9d6ACLcBGAsYHQ/s2048/14608924_10207481915946999_6040878363128105882_o.jpg'
    }
]
tema = [
    {
        'Url': '/themes/',
        'img1': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (1).jpg',
        'title1': 'Galaxy Android',
        'content1': 'Aplikasi android Galaxy themes',
        'video1': 'https://www.youtube.com/watch?v=UsKbCzS3k4E',
        'img2': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (2).jpg',
        'title2': 'All blues Android',
        'content2': 'Aplikasi android all blues themes ',
        'video2': 'https://www.youtube.com/watch?v=B42-d-EWgm8',
        'img3': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (3).jpg',
        'title3': 'Groll Android',
        'content3': 'Aplikasi android Grool template ',
        'video3': 'https://www.youtube.com/watch?v=rfZQQQG7Mjs',
        'img4': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (4).jpg',
        'title4': 'Greeny Android',
        'content4': 'Aplikasi android greeny themes template',
        'video4': 'https://www.youtube.com/watch?v=3m-tjfjDXvk',
        'img5': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (5).jpg',
        'title5': 'Red Android',
        'content5': 'Aplikasi android Red template',
        'video5': 'https://www.youtube.com/watch?v=-ISAQROr5MM',
        'img6': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (6).jpg',
        'title6': 'Slider Pink Android',
        'content6': 'Aplikasi android slider pink template ',
        'video6': 'https://www.youtube.com/watch?v=STf3zxcpRDE',
        'img7': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (7).jpg',
        'title7': 'Dark Night Android',
        'content7': 'Aplikasi android dark night themes',
        'video7': 'https://www.youtube.com/watch?v=5FDAcCNdYNo',
        'img8': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (8).jpg',
        'title8': 'Fun Blue NIte Android',
        'content8': 'Aplikasi android fun blue nite themes ',
        'video8': 'https://www.youtube.com/watch?v=iBAUS5jf2V0',
        'img9': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (9).jpg',
        'title9': 'Dakr Peteng Android',
        'content9': 'Aplikasi android Dark peteng template ',
        'video9': 'https://www.youtube.com/watch?v=zb45J14gNUY',
        'img10': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (10).jpg',
        'title10': 'The Blous Android',
        'content10': 'Aplikasi android the blous themes ',
        'video10': 'https://www.youtube.com/watch?v=AQaAal2AbZw',
        'img11': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (11).jpg',
        'title11': 'Just Green Android',
        'content11': 'Aplikasi android just green template ',
        'video11': 'https://www.youtube.com/watch?v=v7_Ub0lyvAU',
        'img12': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (12).jpg',
        'title12': 'Sun Green Android',
        'content12': 'Aplikasi android sun green template themes',
        'video12': 'https://www.youtube.com/watch?v=-kht4_wnXho',
        'img13': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (13).jpg',
        'title13': 'Red OWl Android',
        'content13': 'Aplikasi android Red on Owl themes template',
        'video13': 'https://www.youtube.com/watch?v=Xh9dwOPBljc',
        'img14': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (14).jpg',
        'title14': 'Red Black Premium Android',
        'content14': 'Aplikasi android red black premium',
        'video14': 'https://www.youtube.com/watch?v=FnMghNtfap8',
        'img15': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (15).jpg',
        'title15': 'Jus SLider Android',
        'content15': 'Aplikasi android just slider themes',
        'video15': 'https://www.youtube.com/watch?v=335YTXpKx4Q',
        'img16': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (16).jpg',
        'title16': 'Android Murah',
        'content16': 'Aplikasi android murah meriah themes',
        'video16': 'https://www.youtube.com/watch?v=1zAHrcDytAc',
        'img17': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (17).jpg',
        'title17': 'Sip Fun Themes Android',
        'content17': 'Aplikasi android sip konsep fun ',
        'video17': 'https://www.youtube.com/watch?v=IhgbUFapWB0',
        'img18': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (18).jpg',
        'title18': 'Old School Retro Android',
        'content18': 'Aplikasi android old school retro themes',
        'video18': 'https://www.youtube.com/watch?v=12PUI-K-d8Y',
        'img19': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (19).jpg',
        'title19': 'Black Red Android',
        'content19': 'Aplikasi android black on red themes ',
        'video19': 'https://www.youtube.com/watch?v=zb45J14gNUY',
        'img20': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (20).jpg',
        'title20': 'Call the black Android',
        'content20': 'Aplikasi android call the black themes ',
        'video20': 'https://www.youtube.com/watch?v=FnMghNtfap8',
        'img21': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (21).jpg',
        'title21': 'Couliners Android',
        'content21': 'Aplikasi android couliners ',
        'video21': 'https://www.youtube.com/watch?v=_9dmDzonKPA',
        'img22': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (22).jpg',
        'title22': 'Android DX',
        'content22': 'Aplikasi android Profesional ',
        'video22': 'https://www.youtube.com/watch?v=hvzjFQ7nvoQ',
        'img23': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (23).jpg',
        'title23': 'Android Neon',
        'content23': 'Aplikasi android konsep neon ',
        'video23': 'https://www.youtube.com/watch?v=OIO88F0C4Ss',
        'img24': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (24).jpg',
        'title24': 'Salon SPA Android App',
        'content24': 'Aplikasi android salon spa klinik kecantikan ',
        'video24': 'https://www.youtube.com/watch?v=mTWw-zORXH4',
        'img25': 'https://axcora.com/img/android/themes/pembuatan aplikasi android (25).jpg',
        'title25': 'Aplikasi Android Robopos',
        'content25': 'Aplikasi android dengan javascript views ',
        'video25': 'https://www.youtube.com/watch?v=koCi_9Ek0AM',
    }
]

@app.route('/')
def home():
    return render_template(
        'home.html', 
        content=content, 
        title='Pembuatan aplikasi android', 
        description='Butuh aplikasi android keren dan murah wajib masuk sini , berbagai pilihan siap pakai untuk toko shop salon restoran cafe company profile dan lain nya'
        )

@app.route('/about/')
def about():
    return render_template('about.html',
    aboutu=aboutu, 
    title='Seberapa penting nya memiliki aplikasi Android', 
    description='Mengapa kita butuh memiliki aplikasi android apa fungsi dan tujuan nya sendiri kita akan ulas disini.'
    )

@app.route('/themes/')
def themes():
    return render_template('themes.html',
    tema=tema, 
    title='Pilihan tema untuk pembuatan aplikasi Android', 
    description='Aneka tema android bisa anda pilih dan gunakan dalam pembuatan aplikasi android mu.'
    )
    
@app.route('/pricing/')
def pricing():
    return render_template('pricing.html',
    prices=prices, 
    title='Daftar harga layanan pembuatan aplikasi Android', 
    description='Pembuatan aplikasi android dengan harga murah hanya disini.'
    )

@app.route('/native/')
def native():
    return render_template('native.html', 
    content=content, 
    title='Pembuatan Aplikasi android native java kotlin',
    description='Buat aplikasi android yang super slim dengan ukuran minimalis maka android native adalah jawaban nya , saatnya sekarang gunakan layanan android app bundle native ini.')

@app.route('/flutter-ionic-react/')
def flutter():
    return render_template('flutter-ionic-react.html', 
    content=content, 
    title='Pembuatan Aplikasi android flutter ionic react native',
    description='Flutter dart maupun ionic angular dan react native adalah technology modern dalam pengembangan dan pembuatan aplikasi android mu.'
    )

@app.route('/webapp/')
def webapp():
    return render_template('webapp.html', 
    content=content, 
    title='Pembuatan Aplikasi android dan website terintegrasi',
    description='Saatnya revolusi digital dimulai dengan pembuatan website, pembuatan aplikasi kasir toko minimarket shop restoran cafe dan akuntansi invoice terintergasi dengan android apps mu.'
    )

@app.route('/webview/')
def webview():
    return render_template('webview.html', 
    content=content, 
    title='Konvert website menjadi aplikasi android',
    description='Butuh dan ingin konvert website mu menjadi sebuah aplikasi android ?? maka layanan webview murah kami ini bisa kamu gunakan.'
    )

@app.route('/pwa/')
def pwa():
    return render_template('pwa.html', 
    content=content, 
    title='Pembuatan Website Single page application plus Aplikasi android',
    description='Semakin mudah dan murah dengan layanan single page app plus android bundle apps dalam satu proses cepat untuk pengembangan nya.'
    )

@app.route('/androidsekolah/')
def andros():
    return render_template('androidsekolah.html', 
    content=content, 
    title='Pembuatan Aplikasi android untuk sekolah',
    description='Saatnya sekolah sd smp sma pg tk dan universitas memiliki sebuah website pun dengan aplikasi android untuk memudahkan proses belajar mengajar.'
    )

@app.route('/toko/')
def toko():
    return render_template('toko.html', 
    content=content, 
    title='Aplikasi android untuk toko shop outlet mu',
    description='Solusi terbaik dalam kebutuhan untuk toko shop outlet store dengan aplikasi android toko shop layanan kami.',
        )

@app.route('/resto/')
def resto():
    return render_template('resto.html', 
    content=content, 
    title='Aplikasi android restoran cafe rumah makan.',
    description='Pembuatan aplikasi android untuk pengusaha kuliner agar memudahkan dalam melayani pelanggan dengan cepat.',
     )

@app.route('/company/')
def company():
    return render_template('company.html', 
    content=content, 
    title='Pembuatan Aplikasi dan website company profile',
    description='Semakin elegan terpercaya dan mewah dengan website company profile include dengan aplikasi android apps dalam kebutuhan pengembangan system webapp perusahaan .'
    )

@app.route('/booking/')
def booking():
    return render_template('booking.html', 
    content=content, 
    title='Aplikasi untuk salon spa, hotel dengan kebutuhan booking system',
    description='Buat dan kembangkan website booking system yang terintegrasi dengan aplikasi android untuk memberikan kemudahan kepada pelanggan dalam melakukan booking secara online.'
    )

@app.route('/artwork/')
def artwork():
    return render_template('artwork.html', 
    content=content, 
    title='Pembuatan Aplikasi android gallery seni',
    description='Special untuk pekerja seni yang ingin menampilkan hasil karya pada website maupun aplikasi android maka layanan pembuatan aplikasi android kami layak untuk mu.'
    )


if __name__ == '__main__':
    app.run(debug=True)
