#!/usr/bin/perl
#use utf8;
use CGI;
$query = new CGI;

print $query->header(-charset=>'UTF-8');
print $query->start_html('SCRIPT USANDO MODULO CGI');
open F,">>/tmp/usua-regis";
if(!$query->param) {
        print $query->start_form;
        print $query->h3('Introduzca su nombre');
        print $query->textfield('nombre');
        print $query->h3('Introduzca su apellido');
        print $query->textfield('ape');
        print $query->br;
        print $query->submit;
        print $query->end_form;
        print $query->br;
}
else{
        if (!$query->param('nombre') eq "") {
                print $query->start_form;
                print $query->b('Hola '),$query->param('nombre'),' ',$query->param('ape');
                print F $query->param('nombre'),':',$query->param('ape'),':';
                print $query->br;
                print $query->h3('Introduzca su edad');
                print $query->textfield('edad');
                print $query->submit(-name=>'enviar',-value=>'Enviar');
                print $query->end_form;
                print $query->br;

        }
}


if (!$query->param('enviar') eq ""){
        print $query->start_html;
        print $query->start_form;
        print $query->b('Tiene '),' ', $query->param('edad'),' anios';
        print F $query->param('edad'),'/';
        print $query->end_form;
        print $query->br;
}
