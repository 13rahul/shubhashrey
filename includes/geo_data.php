<?php
/**
 * States, districts, and Maharashtra MIDC industrial areas for CRM dropdowns.
 * Maharashtra: all 36 districts (current official names).
 * Other states: full district lists for major industrial / neighbouring states;
 * remaining states include capital + major industrial districts.
 */
declare(strict_types=1);

/**
 * @return list<string>
 */
function shubh_india_states(): array
{
    return [
        'Andhra Pradesh',
        'Arunachal Pradesh',
        'Assam',
        'Bihar',
        'Chhattisgarh',
        'Goa',
        'Gujarat',
        'Haryana',
        'Himachal Pradesh',
        'Jharkhand',
        'Karnataka',
        'Kerala',
        'Madhya Pradesh',
        'Maharashtra',
        'Manipur',
        'Meghalaya',
        'Mizoram',
        'Nagaland',
        'Odisha',
        'Punjab',
        'Rajasthan',
        'Sikkim',
        'Tamil Nadu',
        'Telangana',
        'Tripura',
        'Uttar Pradesh',
        'Uttarakhand',
        'West Bengal',
        'Andaman and Nicobar Islands',
        'Chandigarh',
        'Dadra and Nagar Haveli and Daman and Diu',
        'Delhi',
        'Jammu and Kashmir',
        'Ladakh',
        'Lakshadweep',
        'Puducherry',
    ];
}

/**
 * @return array<string, list<string>>
 */
function shubh_state_districts_map(): array
{
    return [
        'Maharashtra' => [
            'Ahilyanagar',
            'Akola',
            'Amravati',
            'Beed',
            'Bhandara',
            'Buldhana',
            'Chandrapur',
            'Chhatrapati Sambhajinagar',
            'Dharashiv',
            'Dhule',
            'Gadchiroli',
            'Gondia',
            'Hingoli',
            'Jalgaon',
            'Jalna',
            'Kolhapur',
            'Latur',
            'Mumbai City',
            'Mumbai Suburban',
            'Nagpur',
            'Nanded',
            'Nandurbar',
            'Nashik',
            'Palghar',
            'Parbhani',
            'Pune',
            'Raigad',
            'Ratnagiri',
            'Sangli',
            'Satara',
            'Sindhudurg',
            'Solapur',
            'Thane',
            'Wardha',
            'Washim',
            'Yavatmal',
        ],
        'Gujarat' => [
            'Ahmedabad', 'Amreli', 'Anand', 'Aravalli', 'Banaskantha', 'Bharuch', 'Bhavnagar',
            'Botad', 'Chhota Udaipur', 'Dahod', 'Dang', 'Devbhumi Dwarka', 'Gandhinagar',
            'Gir Somnath', 'Jamnagar', 'Junagadh', 'Kheda', 'Kutch', 'Mahisagar', 'Mehsana',
            'Morbi', 'Narmada', 'Navsari', 'Panchmahal', 'Patan', 'Porbandar', 'Rajkot',
            'Sabarkantha', 'Surat', 'Surendranagar', 'Tapi', 'Vadodara', 'Valsad',
        ],
        'Karnataka' => [
            'Bagalkot', 'Ballari', 'Belagavi', 'Bengaluru Rural', 'Bengaluru Urban', 'Bidar',
            'Chamarajanagar', 'Chikkaballapur', 'Chikkamagaluru', 'Chitradurga', 'Dakshina Kannada',
            'Davanagere', 'Dharwad', 'Gadag', 'Hassan', 'Haveri', 'Kalaburagi', 'Kodagu', 'Kolar',
            'Koppal', 'Mandya', 'Mysuru', 'Raichur', 'Ramanagara', 'Shivamogga', 'Tumakuru',
            'Udupi', 'Uttara Kannada', 'Vijayanagara', 'Vijayapura', 'Yadgir',
        ],
        'Telangana' => [
            'Adilabad', 'Bhadradri Kothagudem', 'Hanamkonda', 'Hyderabad', 'Jagtial', 'Jangaon',
            'Jayashankar Bhupalpally', 'Jogulamba Gadwal', 'Kamareddy', 'Karimnagar', 'Khammam',
            'Kumuram Bheem', 'Mahabubabad', 'Mahabubnagar', 'Mancherial', 'Medak', 'Medchal–Malkajgiri',
            'Mulugu', 'Nagarkurnool', 'Nalgonda', 'Narayanpet', 'Nirmal', 'Nizamabad', 'Peddapalli',
            'Rajanna Sircilla', 'Rangareddy', 'Sangareddy', 'Siddipet', 'Suryapet', 'Vikarabad',
            'Wanaparthy', 'Warangal', 'Yadadri Bhuvanagiri',
        ],
        'Tamil Nadu' => [
            'Ariyalur', 'Chengalpattu', 'Chennai', 'Coimbatore', 'Cuddalore', 'Dharmapuri', 'Dindigul',
            'Erode', 'Kallakurichi', 'Kanchipuram', 'Kanniyakumari', 'Karur', 'Krishnagiri', 'Madurai',
            'Mayiladuthurai', 'Nagapattinam', 'Namakkal', 'Nilgiris', 'Perambalur', 'Pudukkottai',
            'Ramanathapuram', 'Ranipet', 'Salem', 'Sivaganga', 'Tenkasi', 'Thanjavur', 'Theni',
            'Thoothukudi', 'Tiruchirappalli', 'Tirunelveli', 'Tirupathur', 'Tiruppur', 'Tiruvallur',
            'Tiruvannamalai', 'Tiruvarur', 'Vellore', 'Viluppuram', 'Virudhunagar',
        ],
        'Madhya Pradesh' => [
            'Agar Malwa', 'Alirajpur', 'Anuppur', 'Ashoknagar', 'Balaghat', 'Barwani', 'Betul', 'Bhind',
            'Bhopal', 'Burhanpur', 'Chhatarpur', 'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar',
            'Dindori', 'Guna', 'Gwalior', 'Harda', 'Indore', 'Jabalpur', 'Jhabua', 'Katni', 'Khandwa',
            'Khargone', 'Mandla', 'Mandsaur', 'Morena', 'Narsinghpur', 'Neemuch', 'Niwari', 'Panna',
            'Raisen', 'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Satna', 'Sehore', 'Seoni', 'Shahdol',
            'Shajapur', 'Sheopur', 'Shivpuri', 'Sidhi', 'Singrauli', 'Tikamgarh', 'Ujjain', 'Umaria',
            'Vidisha',
        ],
        'Rajasthan' => [
            'Ajmer', 'Alwar', 'Banswara', 'Baran', 'Barmer', 'Bharatpur', 'Bhilwara', 'Bikaner',
            'Bundi', 'Chittorgarh', 'Churu', 'Dausa', 'Dholpur', 'Dungarpur', 'Hanumangarh', 'Jaipur',
            'Jaisalmer', 'Jalore', 'Jhalawar', 'Jhunjhunu', 'Jodhpur', 'Karauli', 'Kota', 'Nagaur',
            'Pali', 'Pratapgarh', 'Rajsamand', 'Sawai Madhopur', 'Sikar', 'Sirohi', 'Sri Ganganagar',
            'Tonk', 'Udaipur',
        ],
        'Uttar Pradesh' => [
            'Agra', 'Aligarh', 'Ambedkar Nagar', 'Amethi', 'Amroha', 'Auraiya', 'Ayodhya', 'Azamgarh',
            'Bagpat', 'Bahraich', 'Ballia', 'Balrampur', 'Banda', 'Barabanki', 'Bareilly', 'Basti',
            'Bhadohi', 'Bijnor', 'Budaun', 'Bulandshahr', 'Chandauli', 'Chitrakoot', 'Deoria', 'Etah',
            'Etawah', 'Farrukhabad', 'Fatehpur', 'Firozabad', 'Gautam Buddha Nagar', 'Ghaziabad',
            'Ghazipur', 'Gonda', 'Gorakhpur', 'Hamirpur', 'Hapur', 'Hardoi', 'Hathras', 'Jalaun',
            'Jaunpur', 'Jhansi', 'Kannauj', 'Kanpur Dehat', 'Kanpur Nagar', 'Kasganj', 'Kaushambi',
            'Kheri', 'Kushinagar', 'Lalitpur', 'Lucknow', 'Maharajganj', 'Mahoba', 'Mainpuri', 'Mathura',
            'Mau', 'Meerut', 'Mirzapur', 'Moradabad', 'Muzaffarnagar', 'Pilibhit', 'Pratapgarh',
            'Prayagraj', 'Raebareli', 'Rampur', 'Saharanpur', 'Sambhal', 'Sant Kabir Nagar',
            'Shahjahanpur', 'Shamli', 'Shravasti', 'Siddharthnagar', 'Sitapur', 'Sonbhadra',
            'Sultanpur', 'Unnao', 'Varanasi',
        ],
        'Delhi' => [
            'Central Delhi', 'East Delhi', 'New Delhi', 'North Delhi', 'North East Delhi',
            'North West Delhi', 'Shahdara', 'South Delhi', 'South East Delhi', 'South West Delhi',
            'West Delhi',
        ],
        'Haryana' => [
            'Ambala', 'Bhiwani', 'Charkhi Dadri', 'Faridabad', 'Fatehabad', 'Gurugram', 'Hisar',
            'Jhajjar', 'Jind', 'Kaithal', 'Karnal', 'Kurukshetra', 'Mahendragarh', 'Nuh', 'Palwal',
            'Panchkula', 'Panipat', 'Rewari', 'Rohtak', 'Sirsa', 'Sonipat', 'Yamunanagar',
        ],
        'Punjab' => [
            'Amritsar', 'Barnala', 'Bathinda', 'Faridkot', 'Fatehgarh Sahib', 'Fazilka', 'Ferozepur',
            'Gurdaspur', 'Hoshiarpur', 'Jalandhar', 'Kapurthala', 'Ludhiana', 'Malerkotla', 'Mansa',
            'Moga', 'Pathankot', 'Patiala', 'Rupnagar', 'Sahibzada Ajit Singh Nagar', 'Sangrur',
            'Shahid Bhagat Singh Nagar', 'Sri Muktsar Sahib', 'Tarn Taran',
        ],
        'Goa' => ['North Goa', 'South Goa'],
        'Chhattisgarh' => [
            'Balod', 'Baloda Bazar', 'Balrampur', 'Bastar', 'Bemetara', 'Bijapur', 'Bilaspur',
            'Dantewada', 'Dhamtari', 'Durg', 'Gariaband', 'Gaurela-Pendra-Marwahi', 'Janjgir-Champa',
            'Jashpur', 'Kabirdham', 'Kanker', 'Kondagaon', 'Korba', 'Korea', 'Mahasamund', 'Manendragarh',
            'Mohla-Manpur', 'Mungeli', 'Narayanpur', 'Raigarh', 'Raipur', 'Rajnandgaon', 'Sakti',
            'Sarangarh-Bilaigarh', 'Sukma', 'Surajpur', 'Surguja',
        ],
        'Odisha' => [
            'Angul', 'Balangir', 'Balasore', 'Bargarh', 'Bhadrak', 'Boudh', 'Cuttack', 'Deogarh',
            'Dhenkanal', 'Gajapati', 'Ganjam', 'Jagatsinghpur', 'Jajpur', 'Jharsuguda', 'Kalahandi',
            'Kandhamal', 'Kendrapara', 'Kendujhar', 'Khordha', 'Koraput', 'Malkangiri', 'Mayurbhanj',
            'Nabarangpur', 'Nayagarh', 'Nuapada', 'Puri', 'Rayagada', 'Sambalpur', 'Subarnapur',
            'Sundargarh',
        ],
        'West Bengal' => [
            'Alipurduar', 'Bankura', 'Birbhum', 'Cooch Behar', 'Dakshin Dinajpur', 'Darjeeling',
            'Hooghly', 'Howrah', 'Jalpaiguri', 'Jhargram', 'Kalimpong', 'Kolkata', 'Malda',
            'Murshidabad', 'Nadia', 'North 24 Parganas', 'Paschim Bardhaman', 'Paschim Medinipur',
            'Purba Bardhaman', 'Purba Medinipur', 'Purulia', 'South 24 Parganas', 'Uttar Dinajpur',
        ],
        'Andhra Pradesh' => [
            'Alluri Sitharama Raju', 'Anakapalli', 'Anantapur', 'Annamayya', 'Bapatla', 'Chittoor',
            'Dr. B. R. Ambedkar Konaseema', 'East Godavari', 'Eluru', 'Guntur', 'Kakinada', 'Krishna',
            'Kurnool', 'Nandyal', 'NTR', 'Palnadu', 'Parvathipuram Manyam', 'Prakasam', 'Srikakulam',
            'Sri Potti Sriramulu Nellore', 'Sri Sathya Sai', 'Tirupati', 'Visakhapatnam', 'Vizianagaram',
            'West Godavari', 'YSR Kadapa',
        ],
        'Jharkhand' => [
            'Bokaro', 'Chatra', 'Deoghar', 'Dhanbad', 'Dumka', 'East Singhbhum', 'Garhwa', 'Giridih',
            'Godda', 'Gumla', 'Hazaribagh', 'Jamtara', 'Khunti', 'Koderma', 'Latehar', 'Lohardaga',
            'Pakur', 'Palamu', 'Ramgarh', 'Ranchi', 'Sahibganj', 'Seraikela-Kharsawan', 'Simdega',
            'West Singhbhum',
        ],
        'Bihar' => [
            'Araria', 'Arwal', 'Aurangabad', 'Banka', 'Begusarai', 'Bhagalpur', 'Bhojpur', 'Buxar',
            'Darbhanga', 'East Champaran', 'Gaya', 'Gopalganj', 'Jamui', 'Jehanabad', 'Kaimur',
            'Katihar', 'Khagaria', 'Kishanganj', 'Lakhisarai', 'Madhepura', 'Madhubani', 'Munger',
            'Muzaffarpur', 'Nalanda', 'Nawada', 'Patna', 'Purnia', 'Rohtas', 'Saharsa', 'Samastipur',
            'Saran', 'Sheikhpura', 'Sheohar', 'Sitamarhi', 'Siwan', 'Supaul', 'Vaishali', 'West Champaran',
        ],
        'Kerala' => [
            'Alappuzha', 'Ernakulam', 'Idukki', 'Kannur', 'Kasaragod', 'Kollam', 'Kottayam', 'Kozhikode',
            'Malappuram', 'Palakkad', 'Pathanamthitta', 'Thiruvananthapuram', 'Thrissur', 'Wayanad',
        ],
        'Uttarakhand' => [
            'Almora', 'Bageshwar', 'Chamoli', 'Champawat', 'Dehradun', 'Haridwar', 'Nainital',
            'Pauri Garhwal', 'Pithoragarh', 'Rudraprayag', 'Tehri Garhwal', 'Udham Singh Nagar', 'Uttarkashi',
        ],
        'Himachal Pradesh' => [
            'Bilaspur', 'Chamba', 'Hamirpur', 'Kangra', 'Kinnaur', 'Kullu', 'Lahaul and Spiti',
            'Mandi', 'Shimla', 'Sirmaur', 'Solan', 'Una',
        ],
        'Assam' => [
            'Baksa', 'Barpeta', 'Biswanath', 'Bongaigaon', 'Cachar', 'Charaideo', 'Chirang', 'Darrang',
            'Dhemaji', 'Dhubri', 'Dibrugarh', 'Dima Hasao', 'Goalpara', 'Golaghat', 'Hailakandi',
            'Hojai', 'Jorhat', 'Kamrup', 'Kamrup Metropolitan', 'Karbi Anglong', 'Karimganj', 'Kokrajhar',
            'Lakhimpur', 'Majuli', 'Morigaon', 'Nagaon', 'Nalbari', 'Sivasagar', 'Sonitpur', 'South Salmara-Mankachar',
            'Tinsukia', 'Udalguri', 'West Karbi Anglong',
        ],
        'Jammu and Kashmir' => [
            'Anantnag', 'Bandipora', 'Baramulla', 'Budgam', 'Doda', 'Ganderbal', 'Jammu', 'Kathua',
            'Kishtwar', 'Kulgam', 'Kupwara', 'Poonch', 'Pulwama', 'Rajouri', 'Ramban', 'Reasi',
            'Samba', 'Shopian', 'Srinagar', 'Udhampur',
        ],
        'Ladakh' => ['Kargil', 'Leh'],
        'Puducherry' => ['Karaikal', 'Mahe', 'Puducherry', 'Yanam'],
        'Chandigarh' => ['Chandigarh'],
        'Dadra and Nagar Haveli and Daman and Diu' => ['Dadra and Nagar Haveli', 'Daman', 'Diu'],
        'Andaman and Nicobar Islands' => ['Nicobar', 'North and Middle Andaman', 'South Andaman'],
        'Lakshadweep' => ['Lakshadweep'],
        'Sikkim' => ['Gangtok', 'Gyalshing', 'Mangan', 'Namchi', 'Pakyong', 'Soreng'],
        'Tripura' => [
            'Dhalai', 'Gomati', 'Khowai', 'North Tripura', 'Sepahijala', 'South Tripura', 'Unakoti', 'West Tripura',
        ],
        'Meghalaya' => [
            'East Garo Hills', 'East Jaintia Hills', 'East Khasi Hills', 'Eastern West Khasi Hills',
            'North Garo Hills', 'Ri Bhoi', 'South Garo Hills', 'South West Garo Hills', 'South West Khasi Hills',
            'West Garo Hills', 'West Jaintia Hills', 'West Khasi Hills',
        ],
        'Manipur' => [
            'Bishnupur', 'Chandel', 'Churachandpur', 'Imphal East', 'Imphal West', 'Jiribam', 'Kakching',
            'Kamjong', 'Kangpokpi', 'Noney', 'Pherzawl', 'Senapati', 'Tamenglong', 'Tengnoupal', 'Thoubal', 'Ukhrul',
        ],
        'Nagaland' => [
            'Chumoukedima', 'Dimapur', 'Kiphire', 'Kohima', 'Longleng', 'Mokokchung', 'Mon', 'Niuland',
            'Noklak', 'Peren', 'Phek', 'Shamator', 'Tseminyu', 'Tuensang', 'Wokha', 'Zunheboto',
        ],
        'Mizoram' => [
            'Aizawl', 'Champhai', 'Hnahthial', 'Khawzawl', 'Kolasib', 'Lawngtlai', 'Lunglei', 'Mamit',
            'Saitual', 'Serchhip', 'Siaha',
        ],
        'Arunachal Pradesh' => [
            'Anjaw', 'Changlang', 'East Kameng', 'East Siang', 'Itanagar Capital Complex', 'Kamle',
            'Kra Daadi', 'Kurung Kumey', 'Lepa Rada', 'Lohit', 'Longding', 'Lower Dibang Valley',
            'Lower Siang', 'Lower Subansiri', 'Namsai', 'Pakke Kessang', 'Papum Pare', 'Shi Yomi',
            'Siang', 'Tawang', 'Tirap', 'Upper Dibang Valley', 'Upper Siang', 'Upper Subansiri',
            'West Kameng', 'West Siang',
        ],
    ];
}

/**
 * Maharashtra MIDC industrial areas (MIDC EODB registry) + sales aliases.
 * Rebuild via: python scripts/build_maharashtra_midcs.py
 *
 * @return list<string>
 */
function shubh_maharashtra_midc_list(): array
{
    $list = [
        'Achalpur',
        'Addl. Ambernath',
        'Addl. Ambernath Pale Ph-3',
        'Addl. Amravati (Textile Park)',
        'Addl. Chandrapur',
        'Addl. Dharashiv',
        'Addl. Dhule',
        'Addl. Dindori',
        'Addl. Jalgaon',
        'Addl. Jalna Ph-1',
        'Addl. Jalna Ph-2',
        'Addl. Jalna Ph-3',
        'Addl. Kurkumbh (Patas)',
        'Addl. Latur',
        'Addl. Mahad',
        'Addl. Murbad',
        'Addl. Nandurbar (Bhaler)',
        'Addl. Palus (Wine Park)',
        'Addl. Patalganga',
        'Addl. Phaltan',
        'Addl. Sinnar (SEZ)',
        'Addl. Yavatmal',
        'Aheri (Mini)',
        'Ahilyanagar',
        'Ahmedpur (Mini)',
        'Airoli MIDC',
        'Ajara',
        'Akola',
        'Akola (Central Government Growth Center)',
        'Akot (Mini)',
        'Ambad',
        'Ambad (Mini)',
        'Ambad MIDC (Nashik)',
        'Ambernath',
        'Ambernath MIDC',
        'Amravati',
        'Anjangaon (Mini)',
        'Ashti (Mini)',
        'Ausa',
        'Badlapur',
        'Balapur (Mini)',
        'Baramati',
        'Baramati MIDC',
        'Baramati Ph-2',
        'Barshi',
        'Barshi Takli (Mini)',
        'Basmat (Mini)',
        'Beed',
        'Bhadravati (Major)',
        'Bhadravati (Mini)',
        'Bhandara',
        'Bhatkuli (Mini)',
        'Bhigwan',
        'Bhivapur (Mini)',
        'Bhokar',
        'Bhokardan',
        'Bhoom (Mini)',
        'Bhosari MIDC',
        'Bhusaval',
        'Boisar MIDC',
        'Brahmanvel',
        'Buldhana (Mini)',
        'Butibori',
        'Butibori Five Star',
        'Butibori MIDC',
        'Butibori Ph-2',
        'Chakan MIDC',
        'Chakan Ph-1',
        'Chakan Ph-2',
        'Chakan Ph-3',
        'Chakan Ph-4',
        'Chakan Ph-5',
        'Chalisgaon',
        'Chandrapur',
        'Chandrapur Tadali (CGGC)',
        'Chandur Railway (Mini)',
        'Chhatrapati Sambhajinagar (Estate)',
        'Chikalthana',
        'Chikalthana MIDC',
        'Chikhali',
        'Chimur (Mini)',
        'Chincholi',
        'Chinchwad MIDC',
        'Dabhol',
        'Dapoli',
        'Darwha (Mini)',
        'Daryapur (Mini)',
        'Deglur',
        'Deoli',
        'Deori',
        'Deoulgaon Raja (Mini)',
        'Dhamangaon',
        'Dhanora',
        'Dharashiv',
        'Dharni (Mini)',
        'Dharur (Mini)',
        'Dhule',
        'Digras (Mini)',
        'Dindori',
        'Dombivli',
        'Dombivli MIDC',
        'Gadchiroli',
        'Gadhinglaj',
        'Gane-Khadpoli',
        'Gangakhed (Mini)',
        'Ghatanji (Mini)',
        'Ghugus',
        'Gokul-Shirgaon',
        'Gondia',
        'Gondpimpri (Mini)',
        'Goregaon (Mini)',
        'Halkarni',
        'Hinganghat (Mini)',
        'Hingna',
        'Hingna MIDC (Nagpur)',
        'Hingoli',
        'Hinjawadi Ph-1',
        'Hinjawadi Ph-2',
        'Hinjawadi Ph-3',
        'Hinjawadi Ph-4',
        'Indapur',
        'Islampur',
        'Jafrabad (Mini)',
        'Jalgaon (Estate)',
        'Jalna (Estate)',
        'Jamkhed',
        'Jath (Mini)',
        'Jejuri',
        'Jintur',
        'Kadegaon (Mini)',
        'Kagal Hatkanangale Five Star',
        'Kagal-Hatkanangale Five Star',
        'Kalamb (Mini)',
        'Kalamnuri (Mini)',
        'Kalmeshwar',
        'Kalyan-Bhiwandi',
        'Kamti Kanhan',
        'Kandhar (Mini)',
        'Karad',
        'Karad MIDC',
        'Karanja (Mini)',
        'Karmala',
        'Katol',
        'Kavathe-Mahankal',
        'Kelapur Pandharkawada',
        'Khamgaon',
        'Khandala Ph-1',
        'Khandala Ph-2',
        'Khandala Ph-3',
        'Kharadi Knowledge Park',
        'Khed SEZ (KEIPL)',
        'Kherdi-Chiplun',
        'Khultabad (Mini)',
        'Kinwat',
        'Koregaon',
        'Krushnur (SEZ) (Pharma)',
        'Kudal',
        'Kuhi (Mini)',
        'Kurduwadi',
        'Kurkheda',
        'Kurkumbh',
        'Kurkumbh MIDC',
        'Lakhandur',
        'Latur',
        'Lonand',
        'Lonar (Mini)',
        'Lote Parshuram MIDC',
        'Lote-Parshuram',
        'Mahad',
        'Mahad MIDC',
        'Mahagaon (Mini)',
        'Mahape MIDC',
        'Majalgaon',
        'Malegaon (Mini)',
        'Malegaon (Textile Park)',
        'Malkapur',
        'Mangalwedha',
        'Mangrulpir (Mini)',
        'Manora (Mini)',
        'Maregaon (Mini)',
        'Marol',
        'Marol (Samruddhi Venture Park)',
        'Mehekar (Mini)',
        'Mhaswad',
        'Mira',
        'Mohadi (Mini)',
        'Morgaon Arjuni (Mini)',
        'Morshi (Mini)',
        'Mudkhed',
        'Mul',
        'Murbad',
        'Murtizapur',
        'Nagbhid',
        'Nagothane',
        'Nanded',
        'Nandgaon-Khandeshwar (Mini)',
        'Nardana Ph-1',
        'Nardana Ph-2',
        'Narkhed (Mini)',
        'Nashik (IT Park)',
        'Nashik-Ambad',
        'Nashik-Satpur',
        'Navapur',
        'Newasa',
        'Nilanga (Mini)',
        'Non-MIDC Industrial Estate',
        'Other / Outside MIDC',
        'Paithan MIDC',
        'Palus (Mini)',
        'Pandare',
        'Parbhani',
        'Parshivni (Mini)',
        'Partur',
        'Patalganga',
        'Patalganga Borivali',
        'Patalganga MIDC',
        'Patan',
        'Patoda (Mini)',
        'Patur (Mini)',
        'Pauni (Mini)',
        'Peth',
        'Phaltan',
        'Phaltan (SEZ)',
        'Phaltan MIDC',
        'Pimpri MIDC',
        'Pimpri-Chinchwad',
        'Pimpri-Chinchwad MIDC',
        'Pusad',
        'Rabale MIDC',
        'Rahuri',
        'Rajiv Gandhi Infotech Park (Hinjawadi) Ph-1',
        'Rajiv Gandhi Infotech Park (Hinjawadi) Ph-2',
        'Rajiv Gandhi Infotech Park (Hinjawadi) Ph-3',
        'Rajura (Mini)',
        'Ranjangaon',
        'Ranjangaon MIDC',
        'Ranjangaon Ph-1',
        'Ranjangaon Ph-3',
        'Ratnagiri-Mirjole',
        'Risod (Mini)',
        'Roha',
        'Roha MIDC',
        'Sadavali',
        'Samudrapur (Mini)',
        'Sangameshwar (Mini)',
        'Sangli-Miraj',
        'Sangli-Miraj-Kupwad MIDC',
        'Sangrampur (Mini)',
        'Saoner',
        'Satara',
        'Satara MIDC',
        'SEEPZ (SEZ)',
        'Shahade (Mini)',
        'Shalgaon-Bombalewadi',
        'Shendra Five Star',
        'Shendra MIDC',
        'Shendra SEZ',
        'Shirala',
        'Shiroli',
        'Shiroli MIDC (Kolhapur)',
        'Shrirampur',
        'Sindewahi (Mini)',
        'Sinnar',
        'Sinnar Ph-1',
        'Sinnar Ph-2',
        'Sinnar Ph-3',
        'Sinnar Ph-4',
        'Solapur',
        'Solapur MIDC',
        'Supa Parner',
        'Surgana',
        'T.T.C.',
        'Talawade Software Park',
        'Talegaon',
        'Talegaon Floriculture Park',
        'Talegaon MIDC',
        'Taloja',
        'Taloja MIDC',
        'Taloja Ph-2',
        'Tarapur',
        'Tarapur MIDC',
        'Telhara (Mini)',
        'Tembhurni',
        'Thane',
        'Tiroda',
        'Tiwasa (Mini)',
        'TTC MIDC (Trans Thane Creek)',
        'Tumsar (Mini)',
        'Umarga',
        'Umarkhed (Mini)',
        'Umred',
        'Usar',
        'Vaijapur',
        'Vile Bhagad MIDC',
        'Vile-Bhagad',
        'Vinchur',
        'Vita',
        'Wagle Estate',
        'Wai',
        'Waluj',
        'Waluj MIDC',
        'Wani',
        'Wardha',
        'Warora',
        'Warud (Mini)',
        'Washim',
        'Yavatmal',
        'Yeola',
    ];

    $list = array_values(array_unique($list));
    natcasesort($list);
    return array_values($list);
}

/**
 * @return list<string>
 */
function shubh_districts_for_state(string $state): array
{
    $map = shubh_state_districts_map();
    return $map[$state] ?? [];
}

/**
 * Flat unique district list (all mapped states) for filters.
 * @return list<string>
 */
function shubh_all_districts_flat(): array
{
    $all = [];
    foreach (shubh_state_districts_map() as $districts) {
        foreach ($districts as $d) {
            $all[] = $d;
        }
    }
    $all = array_values(array_unique($all));
    natcasesort($all);
    return array_values($all);
}

/**
 * Always available when location is outside a listed MIDC.
 *
 * @return list<string>
 */
function shubh_midc_fallback_options(): array
{
    return ['Other / Outside MIDC', 'Non-MIDC Industrial Estate'];
}

/**
 * MIDC names keyed by Maharashtra district (from data/maharashtra-midcs.csv).
 *
 * @return array<string, list<string>>
 */
function shubh_maharashtra_midcs_by_district(): array
{
    static $cache = null;
    if (is_array($cache)) {
        return $cache;
    }

    $cache = [];
    $csv = dirname(__DIR__) . '/data/maharashtra-midcs.csv';
    if (!is_readable($csv)) {
        return $cache;
    }

    $fh = fopen($csv, 'rb');
    if ($fh === false) {
        return $cache;
    }
    $header = fgetcsv($fh);
    if (!is_array($header)) {
        fclose($fh);
        return $cache;
    }
    $header = array_map(static fn($h) => strtolower(trim((string) $h)), $header);
    $nameIdx = array_search('midc_name', $header, true);
    $distIdx = array_search('district', $header, true);
    if ($nameIdx === false || $distIdx === false) {
        fclose($fh);
        return $cache;
    }

    while (($row = fgetcsv($fh)) !== false) {
        $name = trim((string) ($row[$nameIdx] ?? ''));
        $district = trim((string) ($row[$distIdx] ?? ''));
        if ($name === '' || $district === '') {
            continue;
        }
        if (in_array($name, shubh_midc_fallback_options(), true)) {
            continue;
        }
        $cache[$district][] = $name;
    }
    fclose($fh);

    foreach ($cache as $district => $names) {
        $names = array_values(array_unique($names));
        natcasesort($names);
        $cache[$district] = array_values($names);
    }
    ksort($cache, SORT_NATURAL | SORT_FLAG_CASE);

    return $cache;
}

/**
 * Nested map for cascading dropdowns: state → district → MIDC names.
 *
 * @return array<string, array<string, list<string>>>
 */
function shubh_midcs_by_state_district(): array
{
    return [
        'Maharashtra' => shubh_maharashtra_midcs_by_district(),
    ];
}

/**
 * MIDCs for a selected state + district (plus Outside MIDC options).
 *
 * @return list<string>
 */
function shubh_midcs_for(string $state, string $district): array
{
    $fallback = shubh_midc_fallback_options();
    if ($state === '' || $state === 'all') {
        return $fallback;
    }
    if ($district === '' || $district === 'all') {
        return $fallback;
    }

    $map = shubh_midcs_by_state_district();
    $list = $map[$state][$district] ?? [];
    $out = array_values(array_unique(array_merge($list, $fallback)));
    natcasesort($out);
    return array_values($out);
}
