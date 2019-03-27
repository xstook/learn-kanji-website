cat just_country_codes.txt | xargs -I"{}" bash -c 'grep "\[{}\]" whois_country_codes.txt' | sed "s/\[..\]\t//" > just_countries.txt
