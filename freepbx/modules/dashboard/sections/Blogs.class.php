<?php
// vim: set ai ts=4 sw=4 ft=php:
//
// License for all code of this FreePBX module can be found in the license file inside the module directory
// Copyright 2006-2014 Schmooze Com Inc.

namespace FreePBX\modules\Dashboard\Sections;

class Blogs {
	public $rawname = 'Blogs';

	public function getSections($order) {
		return [];
	}

	public function getContent($section) {
		return '';
	}
}
