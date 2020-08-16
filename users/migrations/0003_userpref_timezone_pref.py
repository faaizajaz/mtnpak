# Generated by Django 3.0.8 on 2020-08-04 08:33

from django.db import migrations
import timezone_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200723_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpref',
            name='timezone_pref',
            field=timezone_utils.fields.TimeZoneField(choices=[('Etc/GMT+12', '(GMT-12:00) Etc/GMT+12'), ('Etc/GMT+11', '(GMT-11:00) Etc/GMT+11'), ('Pacific/Midway', '(GMT-11:00) Pacific/Midway'), ('Pacific/Niue', '(GMT-11:00) Pacific/Niue'), ('Pacific/Pago_Pago', '(GMT-11:00) Pacific/Pago_Pago'), ('Pacific/Samoa', '(GMT-11:00) Pacific/Samoa'), ('US/Samoa', '(GMT-11:00) US/Samoa'), ('Etc/GMT+10', '(GMT-10:00) Etc/GMT+10'), ('HST', '(GMT-10:00) HST'), ('Pacific/Honolulu', '(GMT-10:00) Pacific/Honolulu'), ('Pacific/Johnston', '(GMT-10:00) Pacific/Johnston'), ('Pacific/Rarotonga', '(GMT-10:00) Pacific/Rarotonga'), ('Pacific/Tahiti', '(GMT-10:00) Pacific/Tahiti'), ('US/Hawaii', '(GMT-10:00) US/Hawaii'), ('Pacific/Marquesas', '(GMT-09:30) Pacific/Marquesas'), ('America/Adak', '(GMT-09:00) America/Adak'), ('America/Atka', '(GMT-09:00) America/Atka'), ('Etc/GMT+9', '(GMT-09:00) Etc/GMT+9'), ('Pacific/Gambier', '(GMT-09:00) Pacific/Gambier'), ('US/Aleutian', '(GMT-09:00) US/Aleutian'), ('America/Anchorage', '(GMT-08:00) America/Anchorage'), ('America/Juneau', '(GMT-08:00) America/Juneau'), ('America/Metlakatla', '(GMT-08:00) America/Metlakatla'), ('America/Nome', '(GMT-08:00) America/Nome'), ('America/Sitka', '(GMT-08:00) America/Sitka'), ('America/Yakutat', '(GMT-08:00) America/Yakutat'), ('Etc/GMT+8', '(GMT-08:00) Etc/GMT+8'), ('Pacific/Pitcairn', '(GMT-08:00) Pacific/Pitcairn'), ('US/Alaska', '(GMT-08:00) US/Alaska'), ('America/Creston', '(GMT-07:00) America/Creston'), ('America/Dawson', '(GMT-07:00) America/Dawson'), ('America/Dawson_Creek', '(GMT-07:00) America/Dawson_Creek'), ('America/Ensenada', '(GMT-07:00) America/Ensenada'), ('America/Fort_Nelson', '(GMT-07:00) America/Fort_Nelson'), ('America/Hermosillo', '(GMT-07:00) America/Hermosillo'), ('America/Los_Angeles', '(GMT-07:00) America/Los_Angeles'), ('America/Phoenix', '(GMT-07:00) America/Phoenix'), ('America/Santa_Isabel', '(GMT-07:00) America/Santa_Isabel'), ('America/Tijuana', '(GMT-07:00) America/Tijuana'), ('America/Vancouver', '(GMT-07:00) America/Vancouver'), ('America/Whitehorse', '(GMT-07:00) America/Whitehorse'), ('Canada/Pacific', '(GMT-07:00) Canada/Pacific'), ('Canada/Yukon', '(GMT-07:00) Canada/Yukon'), ('Etc/GMT+7', '(GMT-07:00) Etc/GMT+7'), ('MST', '(GMT-07:00) MST'), ('Mexico/BajaNorte', '(GMT-07:00) Mexico/BajaNorte'), ('PST8PDT', '(GMT-07:00) PST8PDT'), ('US/Arizona', '(GMT-07:00) US/Arizona'), ('US/Pacific', '(GMT-07:00) US/Pacific'), ('America/Belize', '(GMT-06:00) America/Belize'), ('America/Boise', '(GMT-06:00) America/Boise'), ('America/Cambridge_Bay', '(GMT-06:00) America/Cambridge_Bay'), ('America/Chihuahua', '(GMT-06:00) America/Chihuahua'), ('America/Costa_Rica', '(GMT-06:00) America/Costa_Rica'), ('America/Denver', '(GMT-06:00) America/Denver'), ('America/Edmonton', '(GMT-06:00) America/Edmonton'), ('America/El_Salvador', '(GMT-06:00) America/El_Salvador'), ('America/Guatemala', '(GMT-06:00) America/Guatemala'), ('America/Inuvik', '(GMT-06:00) America/Inuvik'), ('America/Managua', '(GMT-06:00) America/Managua'), ('America/Mazatlan', '(GMT-06:00) America/Mazatlan'), ('America/Ojinaga', '(GMT-06:00) America/Ojinaga'), ('America/Regina', '(GMT-06:00) America/Regina'), ('America/Shiprock', '(GMT-06:00) America/Shiprock'), ('America/Swift_Current', '(GMT-06:00) America/Swift_Current'), ('America/Tegucigalpa', '(GMT-06:00) America/Tegucigalpa'), ('America/Yellowknife', '(GMT-06:00) America/Yellowknife'), ('Canada/Mountain', '(GMT-06:00) Canada/Mountain'), ('Canada/Saskatchewan', '(GMT-06:00) Canada/Saskatchewan'), ('Chile/EasterIsland', '(GMT-06:00) Chile/EasterIsland'), ('Etc/GMT+6', '(GMT-06:00) Etc/GMT+6'), ('MST7MDT', '(GMT-06:00) MST7MDT'), ('Mexico/BajaSur', '(GMT-06:00) Mexico/BajaSur'), ('Navajo', '(GMT-06:00) Navajo'), ('Pacific/Easter', '(GMT-06:00) Pacific/Easter'), ('Pacific/Galapagos', '(GMT-06:00) Pacific/Galapagos'), ('US/Mountain', '(GMT-06:00) US/Mountain'), ('America/Atikokan', '(GMT-05:00) America/Atikokan'), ('America/Bahia_Banderas', '(GMT-05:00) America/Bahia_Banderas'), ('America/Bogota', '(GMT-05:00) America/Bogota'), ('America/Cancun', '(GMT-05:00) America/Cancun'), ('America/Cayman', '(GMT-05:00) America/Cayman'), ('America/Chicago', '(GMT-05:00) America/Chicago'), ('America/Coral_Harbour', '(GMT-05:00) America/Coral_Harbour'), ('America/Eirunepe', '(GMT-05:00) America/Eirunepe'), ('America/Guayaquil', '(GMT-05:00) America/Guayaquil'), ('America/Indiana/Knox', '(GMT-05:00) America/Indiana/Knox'), ('America/Indiana/Tell_City', '(GMT-05:00) America/Indiana/Tell_City'), ('America/Jamaica', '(GMT-05:00) America/Jamaica'), ('America/Knox_IN', '(GMT-05:00) America/Knox_IN'), ('America/Lima', '(GMT-05:00) America/Lima'), ('America/Matamoros', '(GMT-05:00) America/Matamoros'), ('America/Menominee', '(GMT-05:00) America/Menominee'), ('America/Merida', '(GMT-05:00) America/Merida'), ('America/Mexico_City', '(GMT-05:00) America/Mexico_City'), ('America/Monterrey', '(GMT-05:00) America/Monterrey'), ('America/North_Dakota/Beulah', '(GMT-05:00) America/North_Dakota/Beulah'), ('America/North_Dakota/Center', '(GMT-05:00) America/North_Dakota/Center'), ('America/North_Dakota/New_Salem', '(GMT-05:00) America/North_Dakota/New_Salem'), ('America/Panama', '(GMT-05:00) America/Panama'), ('America/Porto_Acre', '(GMT-05:00) America/Porto_Acre'), ('America/Rainy_River', '(GMT-05:00) America/Rainy_River'), ('America/Rankin_Inlet', '(GMT-05:00) America/Rankin_Inlet'), ('America/Resolute', '(GMT-05:00) America/Resolute'), ('America/Rio_Branco', '(GMT-05:00) America/Rio_Branco'), ('America/Winnipeg', '(GMT-05:00) America/Winnipeg'), ('Brazil/Acre', '(GMT-05:00) Brazil/Acre'), ('CST6CDT', '(GMT-05:00) CST6CDT'), ('Canada/Central', '(GMT-05:00) Canada/Central'), ('EST', '(GMT-05:00) EST'), ('Etc/GMT+5', '(GMT-05:00) Etc/GMT+5'), ('Jamaica', '(GMT-05:00) Jamaica'), ('Mexico/General', '(GMT-05:00) Mexico/General'), ('US/Central', '(GMT-05:00) US/Central'), ('US/Indiana-Starke', '(GMT-05:00) US/Indiana-Starke'), ('America/Anguilla', '(GMT-04:00) America/Anguilla'), ('America/Antigua', '(GMT-04:00) America/Antigua'), ('America/Aruba', '(GMT-04:00) America/Aruba'), ('America/Asuncion', '(GMT-04:00) America/Asuncion'), ('America/Barbados', '(GMT-04:00) America/Barbados'), ('America/Blanc-Sablon', '(GMT-04:00) America/Blanc-Sablon'), ('America/Boa_Vista', '(GMT-04:00) America/Boa_Vista'), ('America/Campo_Grande', '(GMT-04:00) America/Campo_Grande'), ('America/Caracas', '(GMT-04:00) America/Caracas'), ('America/Cuiaba', '(GMT-04:00) America/Cuiaba'), ('America/Curacao', '(GMT-04:00) America/Curacao'), ('America/Detroit', '(GMT-04:00) America/Detroit'), ('America/Dominica', '(GMT-04:00) America/Dominica'), ('America/Fort_Wayne', '(GMT-04:00) America/Fort_Wayne'), ('America/Grand_Turk', '(GMT-04:00) America/Grand_Turk'), ('America/Grenada', '(GMT-04:00) America/Grenada'), ('America/Guadeloupe', '(GMT-04:00) America/Guadeloupe'), ('America/Guyana', '(GMT-04:00) America/Guyana'), ('America/Havana', '(GMT-04:00) America/Havana'), ('America/Indiana/Indianapolis', '(GMT-04:00) America/Indiana/Indianapolis'), ('America/Indiana/Marengo', '(GMT-04:00) America/Indiana/Marengo'), ('America/Indiana/Petersburg', '(GMT-04:00) America/Indiana/Petersburg'), ('America/Indiana/Vevay', '(GMT-04:00) America/Indiana/Vevay'), ('America/Indiana/Vincennes', '(GMT-04:00) America/Indiana/Vincennes'), ('America/Indiana/Winamac', '(GMT-04:00) America/Indiana/Winamac'), ('America/Indianapolis', '(GMT-04:00) America/Indianapolis'), ('America/Iqaluit', '(GMT-04:00) America/Iqaluit'), ('America/Kentucky/Louisville', '(GMT-04:00) America/Kentucky/Louisville'), ('America/Kentucky/Monticello', '(GMT-04:00) America/Kentucky/Monticello'), ('America/Kralendijk', '(GMT-04:00) America/Kralendijk'), ('America/La_Paz', '(GMT-04:00) America/La_Paz'), ('America/Louisville', '(GMT-04:00) America/Louisville'), ('America/Lower_Princes', '(GMT-04:00) America/Lower_Princes'), ('America/Manaus', '(GMT-04:00) America/Manaus'), ('America/Marigot', '(GMT-04:00) America/Marigot'), ('America/Martinique', '(GMT-04:00) America/Martinique'), ('America/Montreal', '(GMT-04:00) America/Montreal'), ('America/Montserrat', '(GMT-04:00) America/Montserrat'), ('America/Nassau', '(GMT-04:00) America/Nassau'), ('America/New_York', '(GMT-04:00) America/New_York'), ('America/Nipigon', '(GMT-04:00) America/Nipigon'), ('America/Pangnirtung', '(GMT-04:00) America/Pangnirtung'), ('America/Port-au-Prince', '(GMT-04:00) America/Port-au-Prince'), ('America/Port_of_Spain', '(GMT-04:00) America/Port_of_Spain'), ('America/Porto_Velho', '(GMT-04:00) America/Porto_Velho'), ('America/Puerto_Rico', '(GMT-04:00) America/Puerto_Rico'), ('America/Santiago', '(GMT-04:00) America/Santiago'), ('America/Santo_Domingo', '(GMT-04:00) America/Santo_Domingo'), ('America/St_Barthelemy', '(GMT-04:00) America/St_Barthelemy'), ('America/St_Kitts', '(GMT-04:00) America/St_Kitts'), ('America/St_Lucia', '(GMT-04:00) America/St_Lucia'), ('America/St_Thomas', '(GMT-04:00) America/St_Thomas'), ('America/St_Vincent', '(GMT-04:00) America/St_Vincent'), ('America/Thunder_Bay', '(GMT-04:00) America/Thunder_Bay'), ('America/Toronto', '(GMT-04:00) America/Toronto'), ('America/Tortola', '(GMT-04:00) America/Tortola'), ('America/Virgin', '(GMT-04:00) America/Virgin'), ('Brazil/West', '(GMT-04:00) Brazil/West'), ('Canada/Eastern', '(GMT-04:00) Canada/Eastern'), ('Chile/Continental', '(GMT-04:00) Chile/Continental'), ('Cuba', '(GMT-04:00) Cuba'), ('EST5EDT', '(GMT-04:00) EST5EDT'), ('Etc/GMT+4', '(GMT-04:00) Etc/GMT+4'), ('US/East-Indiana', '(GMT-04:00) US/East-Indiana'), ('US/Eastern', '(GMT-04:00) US/Eastern'), ('US/Michigan', '(GMT-04:00) US/Michigan'), ('America/Araguaina', '(GMT-03:00) America/Araguaina'), ('America/Argentina/Buenos_Aires', '(GMT-03:00) America/Argentina/Buenos_Aires'), ('America/Argentina/Catamarca', '(GMT-03:00) America/Argentina/Catamarca'), ('America/Argentina/ComodRivadavia', '(GMT-03:00) America/Argentina/ComodRivadavia'), ('America/Argentina/Cordoba', '(GMT-03:00) America/Argentina/Cordoba'), ('America/Argentina/Jujuy', '(GMT-03:00) America/Argentina/Jujuy'), ('America/Argentina/La_Rioja', '(GMT-03:00) America/Argentina/La_Rioja'), ('America/Argentina/Mendoza', '(GMT-03:00) America/Argentina/Mendoza'), ('America/Argentina/Rio_Gallegos', '(GMT-03:00) America/Argentina/Rio_Gallegos'), ('America/Argentina/Salta', '(GMT-03:00) America/Argentina/Salta'), ('America/Argentina/San_Juan', '(GMT-03:00) America/Argentina/San_Juan'), ('America/Argentina/San_Luis', '(GMT-03:00) America/Argentina/San_Luis'), ('America/Argentina/Tucuman', '(GMT-03:00) America/Argentina/Tucuman'), ('America/Argentina/Ushuaia', '(GMT-03:00) America/Argentina/Ushuaia'), ('America/Bahia', '(GMT-03:00) America/Bahia'), ('America/Belem', '(GMT-03:00) America/Belem'), ('America/Buenos_Aires', '(GMT-03:00) America/Buenos_Aires'), ('America/Catamarca', '(GMT-03:00) America/Catamarca'), ('America/Cayenne', '(GMT-03:00) America/Cayenne'), ('America/Cordoba', '(GMT-03:00) America/Cordoba'), ('America/Fortaleza', '(GMT-03:00) America/Fortaleza'), ('America/Glace_Bay', '(GMT-03:00) America/Glace_Bay'), ('America/Goose_Bay', '(GMT-03:00) America/Goose_Bay'), ('America/Halifax', '(GMT-03:00) America/Halifax'), ('America/Jujuy', '(GMT-03:00) America/Jujuy'), ('America/Maceio', '(GMT-03:00) America/Maceio'), ('America/Mendoza', '(GMT-03:00) America/Mendoza'), ('America/Moncton', '(GMT-03:00) America/Moncton'), ('America/Montevideo', '(GMT-03:00) America/Montevideo'), ('America/Paramaribo', '(GMT-03:00) America/Paramaribo'), ('America/Punta_Arenas', '(GMT-03:00) America/Punta_Arenas'), ('America/Recife', '(GMT-03:00) America/Recife'), ('America/Rosario', '(GMT-03:00) America/Rosario'), ('America/Santarem', '(GMT-03:00) America/Santarem'), ('America/Sao_Paulo', '(GMT-03:00) America/Sao_Paulo'), ('America/Thule', '(GMT-03:00) America/Thule'), ('Antarctica/Palmer', '(GMT-03:00) Antarctica/Palmer'), ('Antarctica/Rothera', '(GMT-03:00) Antarctica/Rothera'), ('Atlantic/Bermuda', '(GMT-03:00) Atlantic/Bermuda'), ('Atlantic/Stanley', '(GMT-03:00) Atlantic/Stanley'), ('Brazil/East', '(GMT-03:00) Brazil/East'), ('Canada/Atlantic', '(GMT-03:00) Canada/Atlantic'), ('Etc/GMT+3', '(GMT-03:00) Etc/GMT+3'), ('America/St_Johns', '(GMT-02:30) America/St_Johns'), ('Canada/Newfoundland', '(GMT-02:30) Canada/Newfoundland'), ('America/Godthab', '(GMT-02:00) America/Godthab'), ('America/Miquelon', '(GMT-02:00) America/Miquelon'), ('America/Noronha', '(GMT-02:00) America/Noronha'), ('Atlantic/South_Georgia', '(GMT-02:00) Atlantic/South_Georgia'), ('Brazil/DeNoronha', '(GMT-02:00) Brazil/DeNoronha'), ('Etc/GMT+2', '(GMT-02:00) Etc/GMT+2'), ('Atlantic/Cape_Verde', '(GMT-01:00) Atlantic/Cape_Verde'), ('Etc/GMT+1', '(GMT-01:00) Etc/GMT+1'), ('Africa/Abidjan', '(GMT+00:00) Africa/Abidjan'), ('Africa/Accra', '(GMT+00:00) Africa/Accra'), ('Africa/Bamako', '(GMT+00:00) Africa/Bamako'), ('Africa/Banjul', '(GMT+00:00) Africa/Banjul'), ('Africa/Bissau', '(GMT+00:00) Africa/Bissau'), ('Africa/Conakry', '(GMT+00:00) Africa/Conakry'), ('Africa/Dakar', '(GMT+00:00) Africa/Dakar'), ('Africa/Freetown', '(GMT+00:00) Africa/Freetown'), ('Africa/Lome', '(GMT+00:00) Africa/Lome'), ('Africa/Monrovia', '(GMT+00:00) Africa/Monrovia'), ('Africa/Nouakchott', '(GMT+00:00) Africa/Nouakchott'), ('Africa/Ouagadougou', '(GMT+00:00) Africa/Ouagadougou'), ('Africa/Sao_Tome', '(GMT+00:00) Africa/Sao_Tome'), ('Africa/Timbuktu', '(GMT+00:00) Africa/Timbuktu'), ('America/Danmarkshavn', '(GMT+00:00) America/Danmarkshavn'), ('America/Scoresbysund', '(GMT+00:00) America/Scoresbysund'), ('Atlantic/Azores', '(GMT+00:00) Atlantic/Azores'), ('Atlantic/Reykjavik', '(GMT+00:00) Atlantic/Reykjavik'), ('Atlantic/St_Helena', '(GMT+00:00) Atlantic/St_Helena'), ('Etc/GMT', '(GMT+00:00) Etc/GMT'), ('Etc/GMT+0', '(GMT+00:00) Etc/GMT+0'), ('Etc/GMT-0', '(GMT+00:00) Etc/GMT-0'), ('Etc/GMT0', '(GMT+00:00) Etc/GMT0'), ('Etc/Greenwich', '(GMT+00:00) Etc/Greenwich'), ('Etc/UCT', '(GMT+00:00) Etc/UCT'), ('Etc/UTC', '(GMT+00:00) Etc/UTC'), ('Etc/Universal', '(GMT+00:00) Etc/Universal'), ('Etc/Zulu', '(GMT+00:00) Etc/Zulu'), ('GMT', '(GMT+00:00) GMT'), ('GMT+0', '(GMT+00:00) GMT+0'), ('GMT-0', '(GMT+00:00) GMT-0'), ('GMT0', '(GMT+00:00) GMT0'), ('Greenwich', '(GMT+00:00) Greenwich'), ('Iceland', '(GMT+00:00) Iceland'), ('UCT', '(GMT+00:00) UCT'), ('UTC', '(GMT+00:00) UTC'), ('Universal', '(GMT+00:00) Universal'), ('Zulu', '(GMT+00:00) Zulu'), ('Africa/Algiers', '(GMT+01:00) Africa/Algiers'), ('Africa/Bangui', '(GMT+01:00) Africa/Bangui'), ('Africa/Brazzaville', '(GMT+01:00) Africa/Brazzaville'), ('Africa/Casablanca', '(GMT+01:00) Africa/Casablanca'), ('Africa/Douala', '(GMT+01:00) Africa/Douala'), ('Africa/El_Aaiun', '(GMT+01:00) Africa/El_Aaiun'), ('Africa/Kinshasa', '(GMT+01:00) Africa/Kinshasa'), ('Africa/Lagos', '(GMT+01:00) Africa/Lagos'), ('Africa/Libreville', '(GMT+01:00) Africa/Libreville'), ('Africa/Luanda', '(GMT+01:00) Africa/Luanda'), ('Africa/Malabo', '(GMT+01:00) Africa/Malabo'), ('Africa/Ndjamena', '(GMT+01:00) Africa/Ndjamena'), ('Africa/Niamey', '(GMT+01:00) Africa/Niamey'), ('Africa/Porto-Novo', '(GMT+01:00) Africa/Porto-Novo'), ('Africa/Tunis', '(GMT+01:00) Africa/Tunis'), ('Atlantic/Canary', '(GMT+01:00) Atlantic/Canary'), ('Atlantic/Faeroe', '(GMT+01:00) Atlantic/Faeroe'), ('Atlantic/Faroe', '(GMT+01:00) Atlantic/Faroe'), ('Atlantic/Madeira', '(GMT+01:00) Atlantic/Madeira'), ('Eire', '(GMT+01:00) Eire'), ('Etc/GMT-1', '(GMT+01:00) Etc/GMT-1'), ('Europe/Belfast', '(GMT+01:00) Europe/Belfast'), ('Europe/Dublin', '(GMT+01:00) Europe/Dublin'), ('Europe/Guernsey', '(GMT+01:00) Europe/Guernsey'), ('Europe/Isle_of_Man', '(GMT+01:00) Europe/Isle_of_Man'), ('Europe/Jersey', '(GMT+01:00) Europe/Jersey'), ('Europe/Lisbon', '(GMT+01:00) Europe/Lisbon'), ('Europe/London', '(GMT+01:00) Europe/London'), ('GB', '(GMT+01:00) GB'), ('GB-Eire', '(GMT+01:00) GB-Eire'), ('Portugal', '(GMT+01:00) Portugal'), ('WET', '(GMT+01:00) WET'), ('Africa/Blantyre', '(GMT+02:00) Africa/Blantyre'), ('Africa/Bujumbura', '(GMT+02:00) Africa/Bujumbura'), ('Africa/Cairo', '(GMT+02:00) Africa/Cairo'), ('Africa/Ceuta', '(GMT+02:00) Africa/Ceuta'), ('Africa/Gaborone', '(GMT+02:00) Africa/Gaborone'), ('Africa/Harare', '(GMT+02:00) Africa/Harare'), ('Africa/Johannesburg', '(GMT+02:00) Africa/Johannesburg'), ('Africa/Khartoum', '(GMT+02:00) Africa/Khartoum'), ('Africa/Kigali', '(GMT+02:00) Africa/Kigali'), ('Africa/Lubumbashi', '(GMT+02:00) Africa/Lubumbashi'), ('Africa/Lusaka', '(GMT+02:00) Africa/Lusaka'), ('Africa/Maputo', '(GMT+02:00) Africa/Maputo'), ('Africa/Maseru', '(GMT+02:00) Africa/Maseru'), ('Africa/Mbabane', '(GMT+02:00) Africa/Mbabane'), ('Africa/Tripoli', '(GMT+02:00) Africa/Tripoli'), ('Africa/Windhoek', '(GMT+02:00) Africa/Windhoek'), ('Antarctica/Troll', '(GMT+02:00) Antarctica/Troll'), ('Arctic/Longyearbyen', '(GMT+02:00) Arctic/Longyearbyen'), ('Atlantic/Jan_Mayen', '(GMT+02:00) Atlantic/Jan_Mayen'), ('CET', '(GMT+02:00) CET'), ('Egypt', '(GMT+02:00) Egypt'), ('Etc/GMT-2', '(GMT+02:00) Etc/GMT-2'), ('Europe/Amsterdam', '(GMT+02:00) Europe/Amsterdam'), ('Europe/Andorra', '(GMT+02:00) Europe/Andorra'), ('Europe/Belgrade', '(GMT+02:00) Europe/Belgrade'), ('Europe/Berlin', '(GMT+02:00) Europe/Berlin'), ('Europe/Bratislava', '(GMT+02:00) Europe/Bratislava'), ('Europe/Brussels', '(GMT+02:00) Europe/Brussels'), ('Europe/Budapest', '(GMT+02:00) Europe/Budapest'), ('Europe/Busingen', '(GMT+02:00) Europe/Busingen'), ('Europe/Copenhagen', '(GMT+02:00) Europe/Copenhagen'), ('Europe/Gibraltar', '(GMT+02:00) Europe/Gibraltar'), ('Europe/Kaliningrad', '(GMT+02:00) Europe/Kaliningrad'), ('Europe/Ljubljana', '(GMT+02:00) Europe/Ljubljana'), ('Europe/Luxembourg', '(GMT+02:00) Europe/Luxembourg'), ('Europe/Madrid', '(GMT+02:00) Europe/Madrid'), ('Europe/Malta', '(GMT+02:00) Europe/Malta'), ('Europe/Monaco', '(GMT+02:00) Europe/Monaco'), ('Europe/Oslo', '(GMT+02:00) Europe/Oslo'), ('Europe/Paris', '(GMT+02:00) Europe/Paris'), ('Europe/Podgorica', '(GMT+02:00) Europe/Podgorica'), ('Europe/Prague', '(GMT+02:00) Europe/Prague'), ('Europe/Rome', '(GMT+02:00) Europe/Rome'), ('Europe/San_Marino', '(GMT+02:00) Europe/San_Marino'), ('Europe/Sarajevo', '(GMT+02:00) Europe/Sarajevo'), ('Europe/Skopje', '(GMT+02:00) Europe/Skopje'), ('Europe/Stockholm', '(GMT+02:00) Europe/Stockholm'), ('Europe/Tirane', '(GMT+02:00) Europe/Tirane'), ('Europe/Vaduz', '(GMT+02:00) Europe/Vaduz'), ('Europe/Vatican', '(GMT+02:00) Europe/Vatican'), ('Europe/Vienna', '(GMT+02:00) Europe/Vienna'), ('Europe/Warsaw', '(GMT+02:00) Europe/Warsaw'), ('Europe/Zagreb', '(GMT+02:00) Europe/Zagreb'), ('Europe/Zurich', '(GMT+02:00) Europe/Zurich'), ('Libya', '(GMT+02:00) Libya'), ('MET', '(GMT+02:00) MET'), ('Poland', '(GMT+02:00) Poland'), ('Africa/Addis_Ababa', '(GMT+03:00) Africa/Addis_Ababa'), ('Africa/Asmara', '(GMT+03:00) Africa/Asmara'), ('Africa/Asmera', '(GMT+03:00) Africa/Asmera'), ('Africa/Dar_es_Salaam', '(GMT+03:00) Africa/Dar_es_Salaam'), ('Africa/Djibouti', '(GMT+03:00) Africa/Djibouti'), ('Africa/Juba', '(GMT+03:00) Africa/Juba'), ('Africa/Kampala', '(GMT+03:00) Africa/Kampala'), ('Africa/Mogadishu', '(GMT+03:00) Africa/Mogadishu'), ('Africa/Nairobi', '(GMT+03:00) Africa/Nairobi'), ('Antarctica/Syowa', '(GMT+03:00) Antarctica/Syowa'), ('Asia/Aden', '(GMT+03:00) Asia/Aden'), ('Asia/Amman', '(GMT+03:00) Asia/Amman'), ('Asia/Baghdad', '(GMT+03:00) Asia/Baghdad'), ('Asia/Bahrain', '(GMT+03:00) Asia/Bahrain'), ('Asia/Beirut', '(GMT+03:00) Asia/Beirut'), ('Asia/Damascus', '(GMT+03:00) Asia/Damascus'), ('Asia/Famagusta', '(GMT+03:00) Asia/Famagusta'), ('Asia/Gaza', '(GMT+03:00) Asia/Gaza'), ('Asia/Hebron', '(GMT+03:00) Asia/Hebron'), ('Asia/Istanbul', '(GMT+03:00) Asia/Istanbul'), ('Asia/Jerusalem', '(GMT+03:00) Asia/Jerusalem'), ('Asia/Kuwait', '(GMT+03:00) Asia/Kuwait'), ('Asia/Nicosia', '(GMT+03:00) Asia/Nicosia'), ('Asia/Qatar', '(GMT+03:00) Asia/Qatar'), ('Asia/Riyadh', '(GMT+03:00) Asia/Riyadh'), ('Asia/Tel_Aviv', '(GMT+03:00) Asia/Tel_Aviv'), ('EET', '(GMT+03:00) EET'), ('Etc/GMT-3', '(GMT+03:00) Etc/GMT-3'), ('Europe/Athens', '(GMT+03:00) Europe/Athens'), ('Europe/Bucharest', '(GMT+03:00) Europe/Bucharest'), ('Europe/Chisinau', '(GMT+03:00) Europe/Chisinau'), ('Europe/Helsinki', '(GMT+03:00) Europe/Helsinki'), ('Europe/Istanbul', '(GMT+03:00) Europe/Istanbul'), ('Europe/Kiev', '(GMT+03:00) Europe/Kiev'), ('Europe/Kirov', '(GMT+03:00) Europe/Kirov'), ('Europe/Mariehamn', '(GMT+03:00) Europe/Mariehamn'), ('Europe/Minsk', '(GMT+03:00) Europe/Minsk'), ('Europe/Moscow', '(GMT+03:00) Europe/Moscow'), ('Europe/Nicosia', '(GMT+03:00) Europe/Nicosia'), ('Europe/Riga', '(GMT+03:00) Europe/Riga'), ('Europe/Simferopol', '(GMT+03:00) Europe/Simferopol'), ('Europe/Sofia', '(GMT+03:00) Europe/Sofia'), ('Europe/Tallinn', '(GMT+03:00) Europe/Tallinn'), ('Europe/Tiraspol', '(GMT+03:00) Europe/Tiraspol'), ('Europe/Uzhgorod', '(GMT+03:00) Europe/Uzhgorod'), ('Europe/Vilnius', '(GMT+03:00) Europe/Vilnius'), ('Europe/Zaporozhye', '(GMT+03:00) Europe/Zaporozhye'), ('Indian/Antananarivo', '(GMT+03:00) Indian/Antananarivo'), ('Indian/Comoro', '(GMT+03:00) Indian/Comoro'), ('Indian/Mayotte', '(GMT+03:00) Indian/Mayotte'), ('Israel', '(GMT+03:00) Israel'), ('Turkey', '(GMT+03:00) Turkey'), ('W-SU', '(GMT+03:00) W-SU'), ('Asia/Baku', '(GMT+04:00) Asia/Baku'), ('Asia/Dubai', '(GMT+04:00) Asia/Dubai'), ('Asia/Muscat', '(GMT+04:00) Asia/Muscat'), ('Asia/Tbilisi', '(GMT+04:00) Asia/Tbilisi'), ('Asia/Yerevan', '(GMT+04:00) Asia/Yerevan'), ('Etc/GMT-4', '(GMT+04:00) Etc/GMT-4'), ('Europe/Astrakhan', '(GMT+04:00) Europe/Astrakhan'), ('Europe/Samara', '(GMT+04:00) Europe/Samara'), ('Europe/Saratov', '(GMT+04:00) Europe/Saratov'), ('Europe/Ulyanovsk', '(GMT+04:00) Europe/Ulyanovsk'), ('Europe/Volgograd', '(GMT+04:00) Europe/Volgograd'), ('Indian/Mahe', '(GMT+04:00) Indian/Mahe'), ('Indian/Mauritius', '(GMT+04:00) Indian/Mauritius'), ('Indian/Reunion', '(GMT+04:00) Indian/Reunion'), ('Asia/Kabul', '(GMT+04:30) Asia/Kabul'), ('Asia/Tehran', '(GMT+04:30) Asia/Tehran'), ('Iran', '(GMT+04:30) Iran'), ('Antarctica/Mawson', '(GMT+05:00) Antarctica/Mawson'), ('Asia/Aqtau', '(GMT+05:00) Asia/Aqtau'), ('Asia/Aqtobe', '(GMT+05:00) Asia/Aqtobe'), ('Asia/Ashgabat', '(GMT+05:00) Asia/Ashgabat'), ('Asia/Ashkhabad', '(GMT+05:00) Asia/Ashkhabad'), ('Asia/Atyrau', '(GMT+05:00) Asia/Atyrau'), ('Asia/Dushanbe', '(GMT+05:00) Asia/Dushanbe'), ('Asia/Karachi', '(GMT+05:00) Asia/Karachi'), ('Asia/Oral', '(GMT+05:00) Asia/Oral'), ('Asia/Qyzylorda', '(GMT+05:00) Asia/Qyzylorda'), ('Asia/Samarkand', '(GMT+05:00) Asia/Samarkand'), ('Asia/Tashkent', '(GMT+05:00) Asia/Tashkent'), ('Asia/Yekaterinburg', '(GMT+05:00) Asia/Yekaterinburg'), ('Etc/GMT-5', '(GMT+05:00) Etc/GMT-5'), ('Indian/Kerguelen', '(GMT+05:00) Indian/Kerguelen'), ('Indian/Maldives', '(GMT+05:00) Indian/Maldives'), ('Asia/Calcutta', '(GMT+05:30) Asia/Calcutta'), ('Asia/Colombo', '(GMT+05:30) Asia/Colombo'), ('Asia/Kolkata', '(GMT+05:30) Asia/Kolkata'), ('Asia/Kathmandu', '(GMT+05:45) Asia/Kathmandu'), ('Asia/Katmandu', '(GMT+05:45) Asia/Katmandu'), ('Antarctica/Vostok', '(GMT+06:00) Antarctica/Vostok'), ('Asia/Almaty', '(GMT+06:00) Asia/Almaty'), ('Asia/Bishkek', '(GMT+06:00) Asia/Bishkek'), ('Asia/Dacca', '(GMT+06:00) Asia/Dacca'), ('Asia/Dhaka', '(GMT+06:00) Asia/Dhaka'), ('Asia/Kashgar', '(GMT+06:00) Asia/Kashgar'), ('Asia/Omsk', '(GMT+06:00) Asia/Omsk'), ('Asia/Qostanay', '(GMT+06:00) Asia/Qostanay'), ('Asia/Thimbu', '(GMT+06:00) Asia/Thimbu'), ('Asia/Thimphu', '(GMT+06:00) Asia/Thimphu'), ('Asia/Urumqi', '(GMT+06:00) Asia/Urumqi'), ('Etc/GMT-6', '(GMT+06:00) Etc/GMT-6'), ('Indian/Chagos', '(GMT+06:00) Indian/Chagos'), ('Asia/Rangoon', '(GMT+06:30) Asia/Rangoon'), ('Asia/Yangon', '(GMT+06:30) Asia/Yangon'), ('Indian/Cocos', '(GMT+06:30) Indian/Cocos'), ('Antarctica/Davis', '(GMT+07:00) Antarctica/Davis'), ('Asia/Bangkok', '(GMT+07:00) Asia/Bangkok'), ('Asia/Barnaul', '(GMT+07:00) Asia/Barnaul'), ('Asia/Ho_Chi_Minh', '(GMT+07:00) Asia/Ho_Chi_Minh'), ('Asia/Hovd', '(GMT+07:00) Asia/Hovd'), ('Asia/Jakarta', '(GMT+07:00) Asia/Jakarta'), ('Asia/Krasnoyarsk', '(GMT+07:00) Asia/Krasnoyarsk'), ('Asia/Novokuznetsk', '(GMT+07:00) Asia/Novokuznetsk'), ('Asia/Novosibirsk', '(GMT+07:00) Asia/Novosibirsk'), ('Asia/Phnom_Penh', '(GMT+07:00) Asia/Phnom_Penh'), ('Asia/Pontianak', '(GMT+07:00) Asia/Pontianak'), ('Asia/Saigon', '(GMT+07:00) Asia/Saigon'), ('Asia/Tomsk', '(GMT+07:00) Asia/Tomsk'), ('Asia/Vientiane', '(GMT+07:00) Asia/Vientiane'), ('Etc/GMT-7', '(GMT+07:00) Etc/GMT-7'), ('Indian/Christmas', '(GMT+07:00) Indian/Christmas'), ('Antarctica/Casey', '(GMT+08:00) Antarctica/Casey'), ('Asia/Brunei', '(GMT+08:00) Asia/Brunei'), ('Asia/Choibalsan', '(GMT+08:00) Asia/Choibalsan'), ('Asia/Chongqing', '(GMT+08:00) Asia/Chongqing'), ('Asia/Chungking', '(GMT+08:00) Asia/Chungking'), ('Asia/Harbin', '(GMT+08:00) Asia/Harbin'), ('Asia/Hong_Kong', '(GMT+08:00) Asia/Hong_Kong'), ('Asia/Irkutsk', '(GMT+08:00) Asia/Irkutsk'), ('Asia/Kuala_Lumpur', '(GMT+08:00) Asia/Kuala_Lumpur'), ('Asia/Kuching', '(GMT+08:00) Asia/Kuching'), ('Asia/Macao', '(GMT+08:00) Asia/Macao'), ('Asia/Macau', '(GMT+08:00) Asia/Macau'), ('Asia/Makassar', '(GMT+08:00) Asia/Makassar'), ('Asia/Manila', '(GMT+08:00) Asia/Manila'), ('Asia/Shanghai', '(GMT+08:00) Asia/Shanghai'), ('Asia/Singapore', '(GMT+08:00) Asia/Singapore'), ('Asia/Taipei', '(GMT+08:00) Asia/Taipei'), ('Asia/Ujung_Pandang', '(GMT+08:00) Asia/Ujung_Pandang'), ('Asia/Ulaanbaatar', '(GMT+08:00) Asia/Ulaanbaatar'), ('Asia/Ulan_Bator', '(GMT+08:00) Asia/Ulan_Bator'), ('Australia/Perth', '(GMT+08:00) Australia/Perth'), ('Australia/West', '(GMT+08:00) Australia/West'), ('Etc/GMT-8', '(GMT+08:00) Etc/GMT-8'), ('Hongkong', '(GMT+08:00) Hongkong'), ('PRC', '(GMT+08:00) PRC'), ('ROC', '(GMT+08:00) ROC'), ('Singapore', '(GMT+08:00) Singapore'), ('Australia/Eucla', '(GMT+08:45) Australia/Eucla'), ('Asia/Chita', '(GMT+09:00) Asia/Chita'), ('Asia/Dili', '(GMT+09:00) Asia/Dili'), ('Asia/Jayapura', '(GMT+09:00) Asia/Jayapura'), ('Asia/Khandyga', '(GMT+09:00) Asia/Khandyga'), ('Asia/Pyongyang', '(GMT+09:00) Asia/Pyongyang'), ('Asia/Seoul', '(GMT+09:00) Asia/Seoul'), ('Asia/Tokyo', '(GMT+09:00) Asia/Tokyo'), ('Asia/Yakutsk', '(GMT+09:00) Asia/Yakutsk'), ('Etc/GMT-9', '(GMT+09:00) Etc/GMT-9'), ('Japan', '(GMT+09:00) Japan'), ('Pacific/Palau', '(GMT+09:00) Pacific/Palau'), ('ROK', '(GMT+09:00) ROK'), ('Australia/Adelaide', '(GMT+09:30) Australia/Adelaide'), ('Australia/Broken_Hill', '(GMT+09:30) Australia/Broken_Hill'), ('Australia/Darwin', '(GMT+09:30) Australia/Darwin'), ('Australia/North', '(GMT+09:30) Australia/North'), ('Australia/South', '(GMT+09:30) Australia/South'), ('Australia/Yancowinna', '(GMT+09:30) Australia/Yancowinna'), ('Antarctica/DumontDUrville', '(GMT+10:00) Antarctica/DumontDUrville'), ('Asia/Ust-Nera', '(GMT+10:00) Asia/Ust-Nera'), ('Asia/Vladivostok', '(GMT+10:00) Asia/Vladivostok'), ('Australia/ACT', '(GMT+10:00) Australia/ACT'), ('Australia/Brisbane', '(GMT+10:00) Australia/Brisbane'), ('Australia/Canberra', '(GMT+10:00) Australia/Canberra'), ('Australia/Currie', '(GMT+10:00) Australia/Currie'), ('Australia/Hobart', '(GMT+10:00) Australia/Hobart'), ('Australia/Lindeman', '(GMT+10:00) Australia/Lindeman'), ('Australia/Melbourne', '(GMT+10:00) Australia/Melbourne'), ('Australia/NSW', '(GMT+10:00) Australia/NSW'), ('Australia/Queensland', '(GMT+10:00) Australia/Queensland'), ('Australia/Sydney', '(GMT+10:00) Australia/Sydney'), ('Australia/Tasmania', '(GMT+10:00) Australia/Tasmania'), ('Australia/Victoria', '(GMT+10:00) Australia/Victoria'), ('Etc/GMT-10', '(GMT+10:00) Etc/GMT-10'), ('Pacific/Chuuk', '(GMT+10:00) Pacific/Chuuk'), ('Pacific/Guam', '(GMT+10:00) Pacific/Guam'), ('Pacific/Port_Moresby', '(GMT+10:00) Pacific/Port_Moresby'), ('Pacific/Saipan', '(GMT+10:00) Pacific/Saipan'), ('Pacific/Truk', '(GMT+10:00) Pacific/Truk'), ('Pacific/Yap', '(GMT+10:00) Pacific/Yap'), ('Australia/LHI', '(GMT+10:30) Australia/LHI'), ('Australia/Lord_Howe', '(GMT+10:30) Australia/Lord_Howe'), ('Antarctica/Macquarie', '(GMT+11:00) Antarctica/Macquarie'), ('Asia/Magadan', '(GMT+11:00) Asia/Magadan'), ('Asia/Sakhalin', '(GMT+11:00) Asia/Sakhalin'), ('Asia/Srednekolymsk', '(GMT+11:00) Asia/Srednekolymsk'), ('Etc/GMT-11', '(GMT+11:00) Etc/GMT-11'), ('Pacific/Bougainville', '(GMT+11:00) Pacific/Bougainville'), ('Pacific/Efate', '(GMT+11:00) Pacific/Efate'), ('Pacific/Guadalcanal', '(GMT+11:00) Pacific/Guadalcanal'), ('Pacific/Kosrae', '(GMT+11:00) Pacific/Kosrae'), ('Pacific/Norfolk', '(GMT+11:00) Pacific/Norfolk'), ('Pacific/Noumea', '(GMT+11:00) Pacific/Noumea'), ('Pacific/Pohnpei', '(GMT+11:00) Pacific/Pohnpei'), ('Pacific/Ponape', '(GMT+11:00) Pacific/Ponape'), ('Antarctica/McMurdo', '(GMT+12:00) Antarctica/McMurdo'), ('Antarctica/South_Pole', '(GMT+12:00) Antarctica/South_Pole'), ('Asia/Anadyr', '(GMT+12:00) Asia/Anadyr'), ('Asia/Kamchatka', '(GMT+12:00) Asia/Kamchatka'), ('Etc/GMT-12', '(GMT+12:00) Etc/GMT-12'), ('Kwajalein', '(GMT+12:00) Kwajalein'), ('NZ', '(GMT+12:00) NZ'), ('Pacific/Auckland', '(GMT+12:00) Pacific/Auckland'), ('Pacific/Fiji', '(GMT+12:00) Pacific/Fiji'), ('Pacific/Funafuti', '(GMT+12:00) Pacific/Funafuti'), ('Pacific/Kwajalein', '(GMT+12:00) Pacific/Kwajalein'), ('Pacific/Majuro', '(GMT+12:00) Pacific/Majuro'), ('Pacific/Nauru', '(GMT+12:00) Pacific/Nauru'), ('Pacific/Tarawa', '(GMT+12:00) Pacific/Tarawa'), ('Pacific/Wake', '(GMT+12:00) Pacific/Wake'), ('Pacific/Wallis', '(GMT+12:00) Pacific/Wallis'), ('NZ-CHAT', '(GMT+12:45) NZ-CHAT'), ('Pacific/Chatham', '(GMT+12:45) Pacific/Chatham'), ('Etc/GMT-13', '(GMT+13:00) Etc/GMT-13'), ('Pacific/Apia', '(GMT+13:00) Pacific/Apia'), ('Pacific/Enderbury', '(GMT+13:00) Pacific/Enderbury'), ('Pacific/Fakaofo', '(GMT+13:00) Pacific/Fakaofo'), ('Pacific/Tongatapu', '(GMT+13:00) Pacific/Tongatapu'), ('Etc/GMT-14', '(GMT+14:00) Etc/GMT-14'), ('Pacific/Kiritimati', '(GMT+14:00) Pacific/Kiritimati')], default='Asia/Karachi', max_length=32),
        ),
    ]
