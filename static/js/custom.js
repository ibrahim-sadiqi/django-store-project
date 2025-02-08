function sendArticleComment(articleId){
    var comment = $('#commentText').val();
    var parentId = $('#parentId').val();
    $.get('/article/add-article-comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId
    }).then(res => {
        $('#commentsArea').html(res);
        $('#commentText').val('');
        $('#parentId').val('');
        if (parentId != null && parentId != ''){
            document.getElementById('single_comment_area' + parentId).scrollIntoView({behavior: 'smooth'});
        }else{
            document.getElementById('commentsArea').scrollIntoView({behavior: 'smooth'});
        }
    });

}

function fillParentId(parentId){
    $('#parentId').val(parentId)
    document.getElementById('commentForm').scrollIntoView({behavior: 'smooth'});
}

function filterProducts(){

    const filterPrice = $('#sl2').val();
    const start_price = filterPrice.split(',')[0]
    const end_price = filterPrice.split(',')[1]
    $('#start_price').val(start_price);
    $('#end_price').val(end_price);
    $('#filter_form').submit()
}

function fillPage(page){
    $('#page').val(page);
    $('#filter_form').submit()

}