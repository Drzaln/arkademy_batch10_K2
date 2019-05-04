<?php
    function tes($name, $address, $hobi ,bool $status, $HighSchool, $university, $bahasa, $program){
        $biodata = [
        "name" => $name,
        "address" => $address,
        "hobbies" => $hobi,
        "is_married" => $status,
        "school" => [
            "HighSchool" => $HighSchool,
            "University" => $university,
            ],
        "skills" => [
            "Bahasa" => $bahasa,
            "Pemrograman" => $program,
            ]
        ];
        return json_encode($biodata);
    }
    
    echo tes("Doddy Rizal Novianto", "Jl.inpres 18, Larangan, Tangerang", ["baca","ngoding","sepedaan"], false, ["SMPN 11 Tangerang", "MAN 1 Klaten"], "Universitas Negeri Semarang", ["Indonesia","Inggris"], ["Dart", "Sedikit Python", "Sedikit PHP"]);
?>