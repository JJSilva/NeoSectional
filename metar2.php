<?php
/**
 * Example:
    $metar = new metar('KARB 152053Z 10007KT 6SM -RA OVC019 04/01 A3006 RMK AO2 SLP187 P0000 60000 T00390006 56024');
 *   echo $metar->raw_text . ': ' . $metar->flightCategoryGet() . "\n";
 */
 $arr = array(kmry,ksns,kwvi,ke16,krhv,ksjc,knuq,kpao,ksql,khaf,ksfo,khwd,koak,klvk,kc83,ksba,koxr,kcma,kwhp,kvny,kbur,ksmd,klax,khhr,kemt,kpoc,kcno,kont,kral,ktoa,klgb,kful,ksna,ksli,kf70,kl35,kpsp,ktrm,ksdm,ksee,kokb,kcrq,krnm,kmyf,ksan,kavx);
 foreach ($arr as $key => $val) {
 
 $url = 'http://www.aviationweather.gov/metar/data?ids='.$val.'&format=raw&hours=0&taf=off&layout=off&date=0';
$content = file_get_contents($url);
$start   = '<!-- Data starts here -->';
$end = '<br /><hr width="65%"/>';
$pos = strpos($content, $start);
if ($pos === false) {
    echo "The string '$start' was not found in the string ";
} else {
    echo "The string '$start' was found in the string ";
    echo " and exists at position $pos";
}
$pos2 = strpos($content, $end);
if ($pos2 === false) {
    echo "The string '$end' was not found in the string ";
} else {
    echo "The string '$end' was found in the string ";
    echo " and exists at position $pos2";
}
$count1 = $pos2-$pos;
echo "count: ";
echo $count1;
$posnew = $pos + 25;
$count1new = $count1 - 25;
$metartext = substr($content, $posnew, $count1new);
echo $metartext;

 
     $metar = new metar($metartext);
   echo $metar->raw_text . ': ' . $metar->flightCategoryGet() . "\n"; 
   $flightcategory = $metar->flightCategoryGet();
   echo $flightcategory;
  if ($flightcategory == "MVFR") {$ledcolor[] = "0,0,255";}
    if ($flightcategory == "VFR") {$ledcolor[] = "255,0,0";}
  if ($flightcategory == "IFR") {$ledcolor[] = "0,255,0";} 
    if ($flightcategory == "LIFR") {$ledcolor[] = "0,125,125";}
}
  $result = exec('sudo python yantest.py ' . $ledcolor[0].' '.$ledcolor[1].' '.$ledcolor[2].' '.$ledcolor[3].' '.$ledcolor[4].' '.$ledcolor[5].' '.$ledcolor[6].' '.$ledcolor[7].' '.$ledcolor[8].' '.$ledcolor[9].' '.$ledcolor[10].' '.$ledcolor[11].' '.$ledcolor[12].' '.$ledcolor[13].' '.$ledcolor[14].' '.$ledcolor[15].' '.$ledcolor[16].' '.$ledcolor[17].' '.$ledcolor[18].' '.$ledcolor[19].' '.$ledcolor[20].' '.$ledcolor[21].' '.$ledcolor[22].' '.$ledcolor[23].' '.$ledcolor[24].' '.$ledcolor[25].' '.$ledcolor[26].' '.$ledcolor[27].' '.$ledcolor[28].' '.$ledcolor[29].' '.$ledcolor[30].' '.$ledcolor[31].' '.$ledcolor[32].' '.$ledcolor[33].' '.$ledcolor[34].' '.$ledcolor[35].' '.$ledcolor[36].' '.$ledcolor[37].' '.$ledcolor[38].' '.$ledcolor[39].' '.$ledcolor[40].' '.$ledcolor[41].' '.$ledcolor[42].' '.$ledcolor[43].' '.$ledcolor[44].' '.$ledcolor[45].' '.$ledcolor[46]); 
//  echo "\n";
  
 // echo "out is ".$out; 
 // echo "\n";
 // echo "result is ".$result; 
// echo "\n";

class metar
{
	// public properties
	public $raw_text;
	public $station_id;
	public $observation_time;
	public $visibility_statute_mi;
	public $cloud_ceiling;
	// array to store the metar code patterns
	private $metarCodePatterns = array(
		"visibility_statute_mi"   => "(\d+)SM",
		"clouds"                  => "SKC|CLR|NSC|((FEW|SCT|BKN|OVC)(\d{3}))",
	);
	/**
	 * Constructor
	 *
	 * @param string $metar the raw metar text
	 */
	function __construct($metar)
	{
		$this->raw_text = $metar;
		// obtain the station code and time
		if (preg_match('/^(?<station_id>[[:upper:]]{4}) (?<observation_time>(\d{2})?(\d{4})Z) /', $metar, $matches) === false)
		{
			throw new Exception("Unable to parse station id and observation time out of metar: '$metar'");
		}
		$this->station_id = $matches['station_id'];
		$this->observation_time = $matches['observation_time'];
		// remove the station code and time from the metar
		$metar = str_replace($matches[0], '', $metar);
		// parse remaining metar codes
		foreach ($this->metarCodePatterns as $name => $pattern)
		{
			if (($found = preg_match_all('/\s?' . $pattern . '\s?/', $metar, $matches, PREG_SET_ORDER)) == true)
			{
				switch ($name)
				{
					case 'visibility_statute_mi':
						$this->visibility_statute_mi = $matches[0][1];
						break;
					case 'clouds':
						foreach ($matches as $match)
						{
							// calculate the cloud ceiling
							if (($match[2] == 'BKN' || $match[2] == 'OVC') && ($this->cloud_ceiling === null || $this->cloud_ceiling > $match[3]))
							{
								$this->cloud_ceiling = $match[3];
							}
						}
				}
			}
		}
	}
	/**
	 * Calculate the flight category
	 *
	 * NOTE: based on information from http://aviationweather.gov/static/info/afc.html
	 *
	 * @return string one of the following categories: VFR, MVFR, IFR, LIFR
	 */
	public function flightCategoryGet()
	{
		if ($this->visibility_statute_mi > 5 && ($this->cloud_ceiling === null | $this->cloud_ceiling > 30))
		{
			return 'VFR';
		}
		elseif ($this->visibility_statute_mi >= 3 && $this->cloud_ceiling >= 10)
		{
			return 'MVFR';
		}
		elseif ($this->visibility_statute_mi >= 1 && $this->cloud_ceiling >= 5)
		{
			return 'IFR';
		}
		else
		{
			return 'LIFR';
		}
	}
}