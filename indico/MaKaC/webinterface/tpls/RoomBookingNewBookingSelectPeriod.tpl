<h2 class="page-title">
    ${ _('Book a room') }
</h2>

<ul id="breadcrumbs" style="margin: 0px 0px 0px -15px; padding: 0; list-style: none;">
    <li><span>${ _('Specify Search Criteria') }</span></li>
    <li><span class="current">${ _('Select Available Period') }</span></li>
    <li><span>${ _('Confirm Reservation') }</span></li>
</ul>


<form id="periodForm" method="POST" action="">
    <input type="hidden" name="step" value="2">
    ${ period_form.repeat_step(type='hidden') }
    ${ period_form.repeat_unit(type='hidden') }
    ${ period_form.start_date(type='hidden') }
    ${ period_form.end_date(type='hidden') }
    ${ period_form.skip_conflicts(type='hidden') }
    ${ period_form.room_id() }
</form>

<div style="display:none;">
    <div id='booking-dialog'>
        <div id="booking-dialog-content" class="dialog-content"></div>
    </div>
</div>


${ calendar }