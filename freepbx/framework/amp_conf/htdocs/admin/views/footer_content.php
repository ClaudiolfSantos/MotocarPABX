<?php
global $amp_conf;
$html = '';
$version	 = get_framework_version();
$version = $version ? $version : getversion();
$version_tag = '?load_version=' . urlencode($version);
if ($amp_conf['FORCE_JS_CSS_IMG_DOWNLOAD']) {
  $this_time_append	= '.' . time();
  $version_tag 		.= $this_time_append;
} else {
	$this_time_append = '';
}

$baseUrl = isset($baseUrl) ? $baseUrl : "";

// Brandable logos in footer
$html .= '<div class="col-md-4" id="footer__left__logo__wrapper">
	<a href="'
                . $amp_conf['BRAND_IMAGE_FREEPBX_LINK_FOOT']
                . '" >'
                . '<img id="footer_logo1" src="'.$baseUrl.'/admin/'.$amp_conf['BRAND_IMAGE_FREEPBX_FOOT'].$version_tag
                . '" alt="'.$amp_conf['BRAND_FREEPBX_ALT_FOOT'] .'"/>
	</a>
	</div>';

//text
$html .= '<div class="col-md-4" id="footer_text">';
$html .= '<strong>MotocarPABX</strong>' . br();
$html .= sprintf(_('Copyright &copy; %s Motocar'), date('Y', time()));

//module license
if (!empty($active_modules[$module_name]['license'])) {
  $html .= br() . sprintf(_('Current module licensed under %s'),
  trim($active_modules[$module_name]['license']));
}

//benchmarking
if (isset($amp_conf['DEVEL']) && $amp_conf['DEVEL']) {
	$benchmark_time = number_format(microtime_float() - $benchmark_starttime, 4);
	$html .= '<br><span id="benchmark_time">Page loaded in ' . $benchmark_time . 's</span>';
}
$html .= '</div>';

$html .= '<div class="col-md-4" id="footer__right__logo__wrapper"></div>';
echo $html;
?>
