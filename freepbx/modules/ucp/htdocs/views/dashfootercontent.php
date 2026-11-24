<?php
global $amp_conf;
$html = '';
$version	 = get_framework_version();
$version = $version ?: getversion();
$version_tag = '?load_version=' . urlencode((string) $version);
if ($amp_conf['FORCE_JS_CSS_IMG_DOWNLOAD']) {
	$this_time_append	= '.' . time();
	$version_tag 		.= $this_time_append;
} else {
	$this_time_append = '';
}

// BRAND_IMAGE_FREEPBX_FOOT based on condtion 
$footer_img ='';
if(isset($amp_conf['BRAND_IMAGE_FREEPBX_FOOT']) && !empty($amp_conf['BRAND_IMAGE_FREEPBX_FOOT'])){
$footer_img = $amp_conf['BRAND_IMAGE_FREEPBX_FOOT'];
}else{
	$footer_img = 'images/motocar-logo-footer.png';
}


// Brandable logos in footer
$html .= '<div class="col-md-4">
	<a href="'
	. $amp_conf['BRAND_IMAGE_FREEPBX_LINK_FOOT']
	. '" >'
	. '<img id="footer_logo1" src="' . $footer_img. $version_tag
	. '" alt="' . $amp_conf['BRAND_FREEPBX_ALT_FOOT'] . '"/>
	</a>
	</div>';

//text
$html .= '<div class="col-md-4" id="footer_text">';
$html .= '<strong>MotocarPABX</strong>' . br();
$html .= sprintf(_('Copyright &copy; %s Motocar'), date('Y', time()));

//module license
$module_name??='';
if (!empty($active_modules[$module_name]['license'])) {
	$html .= br() . sprintf(
		_('Current module licensed under %s'),
		trim((string) $active_modules[$module_name]['license'])
	);
}
$benchmark_time??=0;
$benchmark_starttime??=0;
//benchmarking
if (isset($amp_conf['DEVEL']) && $amp_conf['DEVEL']) {
	$benchmark_time = number_format(microtime_float() - $benchmark_starttime, 4);
	$html .= '<br><span id="benchmark_time">Page loaded in ' . $benchmark_time . 's</span>';
}
$html .= '</div>';

$html .= '<div class="col-md-4"></div>';
echo $html;
