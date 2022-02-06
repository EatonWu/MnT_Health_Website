from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from forms import forms


# The index will prompt users for a number of days
# /dayselector/
@login_required(login_url='/healthhacks/login')
def index(request):
    if request.method == "POST":
        form = forms.DayForm(request.POST)

        if form.is_valid():
            # return HttpResponse(form.cleaned_data['day'])
            # instead of returning form data, render the button html file
            if form.cleaned_data['day'] == 1:
                return HttpResponse(
                    "Cardio is recommend 2-3 times a week and for overall cardiovascular health and can done in the form "
                    "of walking, running, biking, ext." +
                    "<br><br>(Option 1) The full body workout is recommended for those who want to increase overall strength and "
                    "don’t have much time in their schedule to workout. This plan consists of a few exercises to "
                    "work each muscle group." + "<br> <br> <b> 3-4 sets of 10-12 reps for all exercises </b>" + "<br><br><b> Full Body Workout:</b>"
                    + "<br> Barbell Deadlift" + "<br> Bench Press" + "<br> Barbell Row" + "<br> Dumbbell curls" +
                    "<br> Barbell Back Squats" + "<br> Rope Pushdowns" + "<br> Lateral Raises")

            elif form.cleaned_data['day'] == 2:
                return HttpResponse(
                    "Cardio is recommend 2-3 times a week and for overall cardiovascular health and can done in the form "
                    "of walking, running, biking, ext." +
                    "<br><br>(Option 1) The full body workout is recommended for those who want to increase overall strength and "
                    "don’t have much time in their schedule to workout. This plan consists of a few exercises to "
                    "work each muscle group.<br> " + "<br> <b> 3-4 sets of 10-12 reps for all exercises </b>" + "<br><br><b> Full Body Day: </b>" +
                    "<br> -Barbell Deadlift" + "<br> -Bench Press" + "<br> -Barbell Row" + "<br> -Dumbbell curls" +
                    "<br> -Barbell Back Squats" + "<br> -Rope Pushdowns" + "<br> -Lateral Raises <br>" + "<br><b> Repeat 2x a week</b>"
                                                                                                         "<br> <br>(Option 2) The Upper Lower Split is a divide and conquer workout split. "
                                                                                                         "With one day being devoted to the upper body and the other being devoted" +
                    " to lower." + "<br><br> <b> 3-4 sets of 10-12 reps for all exercises </b>" + "<br> <br><b> Upper Body Day:</b>" +
                    "<br> -Bench Press" + "<br> -Bent Over Row"
                    + "<br> -Shoulder Press" + "<br> -Lat Pulldown" + "<br> -Tricep Extenstions"
                    + "<br> -Side Lateral Raises" + "<br> -Pushups" + "<br><br><b> Lower Body Day:</b>"
                    + "<br> Front Squats" + "<br> Straight Leg Deadlift" + "<br> Calf Raises" + "<br> Leg Extensions"
                    + "<br> Hamstring Curls" + "<br> Lunges")
            elif form.cleaned_data['day'] == 3:
                return HttpResponse(
                    "Cardio is recommend 2-3 times a week and for overall cardiovascular health and can done in the form "
                    "of walking, running, biking, ext." + "<br><br>(Option 1) This workout plan encompasses multiple muscle groups in the same day. "
                                                          "This style works antagonist muscles to ensure that muscles being worked have alternate rest periods."
                    + "<br> <br> <b> 3-4 sets of 10-12 reps for all exercises </b>" + "<br> <br><b> Day 1: Chest + Back + Abs:</b>" +
                    "<br> Barbell Chest Press " + "<br> Cable Pulldown" + "<br> Barbell Incline Press" + "<br> Barbell Bent Over Row" +
                    "<br> Pushups" + "<br> V-Bar Cable Row" + "<br> Planks" + "<br> Crunches" + "<br> <br><b> Day 2: Shoulder + Arms:</b>" +
                    "<br> Underhand Lat Pulldown" + "<br> Tricep Dips" + "<br> Dumbbell bicep curls" +
                    "<br> Rope push downs" + "<br> Dumbbell shoulder press" + "<br> Side lateral Raises" +
                    "<br> <br><b> Day 3 Legs:</b>" + "<br> Barbell Back Squats" + "<br> Leg Extensions" + "<br> Hip Thrusts" +
                    "<br> Seated Hamstring Curls" + "<br> Bulgarian Split Squats" + "<br> Calf Raises" +
                    "<br> <br>(Option 2) The push/pull/legs split is a very simple training method in which you split your"
                    " body into three parts. And each part is then trained on its own separate day." + "<br> <br>"
                                                                                                       " <b> 3-4 sets of 10-12 reps for all exercises </b>" + "<br> <br><b> Day 1 Push Workout: </b>" + "<br> Seated Dumbbell Shoulder Press"
                    + "<br> Dumbbell Incline Press" + "<br> Body Weight Tricep Dips" + "<br> Rope Tricep Pushdowns"
                    + "<br> Incline Dumbbell Fly" + "<br> Dumbbell Lateral Raises" + "<br> <br><b> Day 2 Pull Workout:</b>"
                    + "<br> Bent Over Cable Row" + "<br> Cable Push Down" + "<br> Dumbbell Shrugs" + "<br> Bicep Curls"
                    + "<br> Hammer Curls" + "<br> Face Pulls" + "<br> <br><b> Day 3 Leg Workout: </b>" + "<br> Barbell Back Squats"
                    + "<br> Seated Leg Extensions" + "<br> Calf Raises" + "<br> Seated Hamstring Curls"
                    + "<br> Bulgarian Split Squats")

            elif form.cleaned_data['day'] == 4:
                return HttpResponse(
                    "Cardio is recommend 2-3 times a week and for overall cardiovascular health and can done in the form "
                    "of walking, running, biking, ext." +
                    "<br><br>(Option 1) The Upper Lower Split is a divide and conquer workout split. "
                    + "With one day being devoted to the upper body and the other being devoted "
                    + "to lower." + "<br> <br> <b> 3-4 sets of 10-12 reps for all exercises </b>" + "<br> <br><b>Day 1 Upper Body Day:</b>" + "<br> Bench Press" +
                    "<br> Bent Over Row"
                    + "<br> Shoulder Press" + "<br> Lat Pulldown" + "<br> Tricep Extenstions"
                    + "<br> Side Lateral Raises" + "<br> Pushups" + "<br><br><b> Day 2 Leg Day:</b>"
                    + "<br> Front Squats" + "<br> Straight Leg Deadlift" + "<br> Calf Raises" + "<br> Leg Extensions"
                    + "<br> Hamstring Curls" + "<br> Lunges" + "<br> <br> <b>Repeat Workout 2x a week</b>")
            elif form.cleaned_data['day'] == 5:
                return HttpResponse(
                    "Cardio is recommend 2-3 times a week and for overall cardiovascular health and can done in the form "
                    "of walking, running, biking, ext." +
                    "<br><br>(Option 1) Push, Pull, Legs, Upper, Lower This workout split combines push,pull, legs which"
                    "works an entire muscle group on one day allowing for up to 3 days of rest and devoting the"
                    "other two days to your upper/lower body." + "<br> <br>"
                    + " <b> 3-4 sets of 10-12 reps for all exercises </b>" + "<br> <br><b> Day 1 Push Workout: </b>" + "<br> Seated Dumbbell Shoulder Press"
                    + "<br> Dumbbell Incline Press" + "<br> Body Weight Tricep Dips" + "<br> Rope Tricep Pushdowns"
                    + "<br> Incline Dumbell Fly" + "<br> Dumbbell Lateral Raises" + "<br> <br><b> Day 2 Pull Workout:</b>"
                    + "<br> Bent Over Cable Row" + "<br> Cable Push Down" + "<br> Dumbbell Shrugs" + "<br> Bicep Curls"
                    + "<br> Hammer Curls" + "<br> Face Pulls" + "<br> <br><b> Day 3 Leg Workout: </b>" + "<br> Barbell Back Squats"
                    + "<br> Seated Leg Extensions" + "<br> Calf Raises" + "<br> Seated Hamstring Curls"
                    + "<br> Bulgarian Split Squats"
                    + "<br> <br> <b>Day 4 Upper Day:</b>" + "<br> Bench Press" + "<br> Bent Over Row"
                    + "<br> Shoulder Press" + "<br> Lat Pulldown" + "<br> Tricep Extenstions"
                    + "<br> Side Lateral Raises" + "<br> Pushups" + "<br><br><b> Day 5 Lower Day:</b>"
                    + "<br> Front Squats" + "<br> Straight Leg Deadlift" + "<br> Calf Raises" + "<br> Leg Extensions"
                    + "<br> Hamstring Curls" + "<br> Lunges" + "<br> <br>" + "(Option 2) One Muscle A Day: This workout split"
                    + " emphasizes a new part of the body each day of working out and allows for optimal rest." + "<br><br> <b> 3-4 sets of 10-12 reps for all exercises </b>"
                    + "<br> <br><b>Day 1 Chest Day: </b>" + "<br> Bench Press" + "<br> Incline Dumbbell Press" + "<br> Lower Cable Flys"
                    + "<br> Upper Cable Flys" + "<br> Pushups" + "<br><br><b> Day 2 Leg Day:</b> " + "<br> Barbell Back Squats"
                    + "<br> Seated Leg Extensions" + "<br> Seated Hamstring Curls" + "<br> Calf Raises" + "<br> Bulgarian Split Squats"
                    + "<br> <br><b> Day 3 Shoulders: </b>" + "<br> Overhead Press" + "<br> Side Lateral Raises" + "<br> Dumbbell Push Press"
                    + "<br> Cable Face Pulls" + "<br><br><b> Day 4 Back Day:</b>" + "<br> Pullups" + "<br> Barbell Bentover Row"
                    + "<br> Lat Pull Downs" + "<br> Farmer Carries" + "<br> Close grip cable rows" + "<br>"
                    + "<br><b> Day 5 Arms: </b>" + "<br> Dumbbell Curls" + "<br> Preacher Curls" + "<br> Hammer Curls"
                    + "<br> Rope Pushdowns" + " <br> Tricep Dips" + "<br> Katana Extensions")
            elif form.cleaned_data['day'] == 6:
                return HttpResponse(
                    "Cardio is recommend 2-3 times a week and for overall cardiovascular health and can done in the form "
                    "of walking, running, biking, ext." + "<br><br>(Option 1) This workout plan encompasses multiple muscle groups in the same day. "
                                                          "This style works antagonist muscles to ensure that muscles being worked have alternate rest periods." +
                    "<br> <br> <b> 3-4 sets of 10-12 reps for all exercises </b>" + "<br> <br><b> Day 1: Chest + Back + Abs:</b>" +
                    "<br> Barbell Chest Press " + "<br> Cable Pulldown" + "<br> Barbell Incline Press" + "<br> Barbell Bent Over Row" +
                    "<br> Pushups" + "<br> V-Bar Cable Row" + "<br> Planks" + "<br> Crunches" + "<br> <br><b> Day 2: Shoulder + Arms:</b>" +
                    "<br> Underhand Lat Pulldown" + "<br> Tricep Dips" + "<br> Dumbbell bicep curls" +
                    "<br> Rope push downs" + "<br> Dumbbell shoulder press" + "<br> Side lateral Raises" +
                    "<br> <br><b> Day 3 Legs:</b>" + "<br> Barbell Back Squats" + "<br> Leg Extensions" + "<br> Hip Thrusts" +
                    "<br> Seated Hamstring Curls" + "<br> Bulgarian Split Squats" + "<br> Calf Raises" + "<br> <br><b> Rest and Repeat 2x per Week</b>" +
                    "<br> <br> (Option 2) The push/pull/legs split is a very simple training method in which you split your"
                    " body into three parts. And each part is then trained on its own separate day." + "<br> <br>"
                    + "<b> 3-4 sets of 10-12 reps for all exercises </b>" + "<br> <br><b> Day 1 Push Workout:</b> " + "<br> Seated Dumbbell Shoulder Press"
                    + "<br> Dumbbell Incline Press" + "<br> Body Weight Tricep Dips" + "<br> Rope Tricep Pushdowns"
                    + "<br> Incline Dumbell Fly" + "<br> Dumbbell Lateral Raises" + "<br> <br><b> Day 2 Pull Workout:</b>"
                    + "<br> Bent Over Cable Row" + "<br> Cable Push Down" + "<br> Dumbbell Shrugs" + "<br> Bicep Curls"
                    + "<br> Hammer Curls" + "<br> Face Pulls" + "<br> <br><b> Day 3 Leg Workout: </b>" + "<br> Barbell Back Squats"
                    + "<br> Seated Leg Extensions" + "<br> Calf Raises" + "<br> Seated Hamstring Curls"
                    + "<br> Bulgarian Split Squats" + "<br> <br><b> Rest and Repeat 2x per Week</b>")
    else:
        form = forms.DayForm()

    return render(request, 'day_selector/index.html', {'form': form})
