from behave import *


@given('home: I am on home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()


@then('home: Check the url to be "{url}"')
def step_impl(context, url):
    context.home_page.verify_page_url(url)


@when('home: I click Fashion Days logo')
def step_impl(context):
    context.home_page.click_logo_img()


@when('home: I hover over "{category}"')
def step_impl(context, category):
    context.home_page.hover_over_menu_category(category)


@then('home: I hover over "{subcategory}"')
def step_impl(context, subcategory):
    context.home_page.hover_over_menu_subcategory(subcategory)