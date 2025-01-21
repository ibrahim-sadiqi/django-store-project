function sendArticleComment(articleId){
    var comment = $('#commentText').val();
    var parentId = $('#parentId').val();
    $.get('/article/add-article-comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId
    }).then(res => {
        console.log(res)
    });

}

function fillParentId(parentId){
    $('#parentId').val(parentId)
    document.getElementById('commentForm').scrollIntoView({behavior: 'smooth'})
}